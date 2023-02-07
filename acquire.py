#standard ds imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#imports
import os
import requests
import datetime

################################## Planet Acquire and CSV Function ############################

def get_planet_data():
    '''
    This function creates a csv of planet data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('planet.csv'):
        df = pd.read_csv('planet.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/planets/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('planet.csv')

    return df


################################## Starships Acquire and CSV Function ############################


def get_starships_data():
    '''
    This function creates a csv of starship data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('starships.csv'):
        df = pd.read_csv('starships.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/starships/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('starships.csv')

    return df



################################## People Acquire and CSV Function ############################


def get_people_data():
    '''
    This function creates a csv of people data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('people.csv'):
        df = pd.read_csv('people.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/people/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('people.csv')

    return df


################################## Germany Acquire and CSV Function ############################


def get_germany_data():
    '''
    This function creates a csv of germany energy data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('opsd_germany_daily.csv'):
        df = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    
    else:
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        df.to_csv('opsd_germany_daily.csv')

    return df