import numpy as np
import pandas as pd

#datetime utilities
from datetime import timedelta, datetime

import os
import acquire


################################################ Prep Store Function ################################################


def prep_store():
    '''
    This function takes in a df and changes date dtypes, resets date as index,
    creates new columns for month, weekday, and total sales
    and returns that as a new pandas dataframe
    '''
    if os.path.isfile('prep_store.csv'):
        df = pd.read_csv('prep_store.csv', index_col=0)

        #assign variable df to acquire function
        df= acquire.all_store_data()

        #change data type on sale_date
        df.sale_date = df.sale_date.astype('datetime64[ns]')
        #reset sale_date as index
        df = df.set_index('sale_date').sort_index()

        #create new colum for month
        df['month'] = df.index.month_name()
        #create new colum for weekday
        df['day_of_week'] = df.index.day_name()
        #create new colum for sale total
        df['sales_total'] = df.sale_amount * df.item_price

    else:
        df = prep_store()
        df.to_csv('prep_store.csv')

    return df


################################################ Convert to Datetime Function ################################################


def convert_to_datetime(df):
    '''
    This function takes in a dataframe
    and converts the sales_date column to a datetime
    '''
    df.sale_date = pd.to_datetime(df.sale_date, infer_datetime_format=True)
    return df


################################################ Plot Distributions Function ################################################


def plot_distributions(df):
    for col in list(df.columns.drop('Date')):
        plt.figure()
        sns.histplot(df[col])
        plt.title('Distribution of {}'.format(col))