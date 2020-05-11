import requests
import pandas as pd


base_url = 'https://python.zach.lol/api/v1'

def get_items_data():
    # uses base url near imports
    ext = '/items'
    response = requests.get(base_url + ext)
    
    # creates json object
    data = response.json()
    df = pd.DataFrame(data['payload']['items'])
    # converts to df
    return df

def get_stores_data():
    # uses base url near imports
    ext = '/stores'
    response = requests.get(base_url + ext)
    
    # creates json object
    data = response.json()
    df = pd.DataFrame(data['payload']['items'])
    return df


def get_sales_data():
    # uses base url near imports
    ext = '/sales'
    response = requests(base_url + ext)
    
    # creates json object
    data = response.json()
    # get first page
    sales_data = data['payload']['sales']
    total_pages = data['payload']['max_page']
    
    while data['payload']['next_page'] is < total_pages:
        url = base_url + data['payload']['next_page']
        r = requests.get(base_url + ext)
        data = r.json()
        sales_data += data['payload']['sales']
        
    df = pd.DataFrame(sales_data)
    return df
            
        

