import pandas as pd
import numpy as np

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import timedelta, datetime

import acquire
import warnings
warnings.filterwarnings('ignore')


# pulls data from acquire and preps it according to our data prep exercise specs
def prep_store_data():
    # acquire data
    store = acquire.get_store_data()
    # convert sales dat to a date type
    store['sale_date'] = pd.to_datetime(store['sale_date'], format='%Y%m%d')
    # set sale dat as index
    store = store.sort_values('sale_date').set_index('sale_date')
    # add day and month columns to data frame
    store['month'] = store.index.strftime('%m-%b')
    store['day_of_week'] = store.index.strftime('%w-%a')
    # add sales_total column to data frame
    store['sales_total'] = store['sale_amount'] * store['item_price']
    # add daily_difference which is the delta of sales total from
    # day to day
    store['daily_difference'] = store.sales_total.diff()
    return store


# pulls german energy data from acquire and preps it according to our data prep exercise specs
def prep_german_energy():
    # Acquire dataframe from acquire module
    df = acquire.german_energy_csv()
    # Set date as date data type and as index
    df = df.reset_index()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').set_index('Date')
    # add month and year columns
    df['month'] = df.index.strftime('%m')
    df['year'] = df.index.strftime('%Y')
    return df
        