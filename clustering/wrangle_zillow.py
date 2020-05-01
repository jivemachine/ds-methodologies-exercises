
from acquire import get_data_from_zillow
from prepare import zillow_single_unit_prop
from prepare import remove_columns
from prepare import handle_missing_values
from prepare import fill_missing_values

def wrangle_zillow_data():
    df = get_data_from_zillow()
    df = zillow_single_unit_prop(df)
    df = remove_columns(df,['calculatedbathnbr','finishedsquarefeet12','fullbathcnt','propertycountylandusecode','unitcnt','structuretaxvaluedollarcnt','landtaxvaluedollarcnt','assessmentyear','propertyzoningdesc'])
    df = handle_missing_values(df)
    df.dropna(inplace=True)
    return df