import pandas as pd
import env


def get_titanic_data():
    url = env.get_url('titanic_db')
    query = '''
    SELECT *
    FROM passengers;
    '''
    df = pd.read_sql(query, url)
    return df



def get_iris_data():
    url = env.get_url("iris_db")
    query = '''
    SELECT * 
    FROM measurements
    JOIN species USING(species_id)
    '''
    df = pd.read_sql(query, url)
    return df