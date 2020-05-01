import pandas as pd
import numpy as np

import env


def get_data_from_zillow():
    query = '''
     SELECT *
    FROM 
        (SELECT 
        pred.parcelid,
        logerror,
        transactiondate
        FROM 
        predictions_2017 AS pred
    JOIN
    (SELECT 
    predictions_2017.parcelid,
    MAX(transactiondate) AS max_trans_date
    FROM predictions_2017
GROUP BY predictions_2017.parcelid) AS pred_agg ON (pred.parcelid=pred_agg.parcelid) AND (pred_agg.max_trans_date=pred.transactiondate)) AS unique_properties
LEFT JOIN properties_2017 AS A USING(parcelid)
LEFT JOIN propertylandusetype USING (propertylandusetypeid)
LEFT JOIN storytype USING (storytypeid)
LEFT JOIN typeconstructiontype USING (typeconstructiontypeid)
LEFT JOIN airconditioningtype USING (airconditioningtypeid)
LEFT JOIN architecturalstyletype USING (architecturalstyletypeid)
LEFT JOIN buildingclasstype USING (buildingclasstypeid)
LEFT JOIN heatingorsystemtype USING (heatingorsystemtypeid)
WHERE latitude IS NOT NULL AND longitude IS NOT NULL;
'''
    df = pd.read_sql(query, env.get_url('zillow'))
    return df





#def get_data_from_zillow():
#    query = '''
#    SELECT *
#    FROM properties_2017
#    LEFT JOIN predictions_2017 USING(parcelid)
#    LEFT JOIN propertylandusetype USING (propertylandusetypeid)
#    LEFT JOIN storytype USING (storytypeid)
#    LEFT JOIN typeconstructiontype USING (typeconstructiontypeid)
#    LEFT JOIN airconditioningtype USING (airconditioningtypeid)
#    LEFT JOIN architecturalstyletype USING (architecturalstyletypeid)
#    LEFT JOIN buildingclasstype USING (buildingclasstypeid)
#    LEFT JOIN heatingorsystemtype USING (heatingorsystemtypeid)
#    WHERE latitude IS NOT NULL AND longitude IS NOT NULL;'''
#    df = pd.read_sql(query, env.get_url('zillow'))
#    return df


def convert_to_series(df):
    '''
    helper function for the summarize function
    that converts a dataframe into a series and grabs 
    the value counts from that dataframe
    '''
    series = pd.Series([])
    for _, col in enumerate(df.columns.values):
        if df[col].dtype == 'object':
            col_count = df[col].value_counts()
        else:
            col_count = df[col].value_counts(bins=10)
        series = series.append(col_count)
    return series

def summarize(df):
    print("******** Info")
    df.info()
    print()
    print("******** Shape {}".format(df.shape))
    print()
    print("******** Describe")      
    print(df.describe)
    print()
    print("******** Value Counts")      
    print(convert_to_series(df))
    
    
# function returns missing rows in data set
def nulls_missing_rows(df):
    missing = df.isnull().sum()
    pct_rows_missing = missing / df.shape[0]*100
    number_missing = pd.DataFrame({'number_rows_missing':missing, 'pct_rows_missing': pct_rows_missing})
    return number_missing

# function returns missing columns in data set
def nulls_missing_columns(df):
    missing = df.isnull().sum(axis=1)
    pct_cols_missing = df.isnull().sum(axis=1) / df.shape[1]*100
    rows_missing = pd.DataFrame({'num_cols_missing': missing, 'pct_cols_missing':pct_cols_missing, 
                                'num_rows':missing })
    return rows_missing