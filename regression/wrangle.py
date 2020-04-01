import pandas as pd
import numpy as np

from env import host, user, password

# function to get the url

def get_db_url(db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

# function that passes my query and my url to return df

def get_data_from_sql():
    query = """
    SELECT customer_id, monthly_charges, tenure, total_charges
    FROM customers
    WHERE contract_type_id = 3;
    """
    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df

# function that rules them all by acquiring and prepping my df for exploration or modeling

def wrangle_telco():
    df = get_data_from_sql()
    df["total_charges"].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df['total_charges'] = df.total_charges.dropna().astype('float')    
    return df