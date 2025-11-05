#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 16:40:26 2025

@author: bchoe
"""

import pandas as pd

url = "https://www.nps.gov/orgs/1207/national-park-visitation-sets-new-record-as-economic-engines.htm"

tables = pd.read_html(url)
len(tables)

tables
# python index, or slicing

df_0 = tables[0]
df_1 = tables[1]


# df_0 = tables[0]

# first row in df_0 as a Series
df_0.iloc[0]

# column as a list
df_0.columns

df_0.columns = df_0.iloc[0]  # Set the first row as column names



df_0[1:]
# df_0[1:3]
df_0 = df_0[1:]

# df_0 = df_0.reset_index() # this does not drop "index" column

df_0 = df_0[1:].reset_index(drop=True)  # Remove the first row & reset index



# %%
# Import the os module to interact with the operating system
import os  

# Set the working directory path
wd_path = '/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/' # Do not choose your personal website folder
os.chdir(wd_path)  # Change the current working directory to wd_path

os.getcwd()  # Retrieve and return the current working directory

# index=False to not write the row index in the CSV output

df_0.to_csv('table.csv', index =False)


# absolute pathname of the file, table.csv
'/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/table.csv'

# pathname of working directory
wd_path = '/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/' 


# relative pathname of the file, table.csv
'table.csv'


# relative pathname of the file, data/table.csv
df_0.to_csv('data/table.csv', index =False)


# %%
# =============================================================================
# Classwork 8
# =============================================================================


# Set-up
import pandas as pd
import os  

# Set the working directory path
wd_path = '/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/' # Do not choose your personal website folder
os.chdir(wd_path)  # Change the current working directory to wd_path



# Question 1
path_url = 'https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php'

df_list = pd.read_html(path_url)
df = df_list[0]



df.info()

# pd.to_datetime(df['Mon-yr'], format='%b-%y')

df['Mon-yr'] = df['Mon-yr'].str.replace('July', 'Jul')

# pd.to_datetime(df['Mon-yr'], format='%b-%y')

df['Mon-yr'] = df['Mon-yr'].str.replace('Sept', 'Sep')
df['Mon-yr'] = pd.to_datetime(df['Mon-yr'], format='%b-%y')
df.info()


# df.to_csv('data/eia_gaspump.csv')
df.to_csv('data/eia_gaspump.csv', 
          index = False)


# Question 2
path_g = 'https://www.geneseo.edu/business/student%20outcomes'
df_g = pd.read_html(path_g)

df_g0 = df_g[0]
df_g1 = df_g[1]
df_g2 = df_g[2]
df_g3 = df_g[3]
df_g4 = df_g[4]

# Cleaning df_g1
# Unit of value is Percent (%)

# removing the first row
df_g1 = df_g1[1:]

# setting the first row as column names
df_g1.columns = df_g1.iloc[0]

# removing the first row, again
df_g1 = df_g1[1:]

# reseting index
df_g1 = df_g1.reset_index(drop = True)
df_g1.info()

# String cleaning
df_g1['5-Year % Change'] = df_g1['5-Year % Change'].str.replace('+', '')

# Convert string data into numeric data (float)
df_g1.columns

df_g1 = (
    df_g1
    .astype(
        {
           '2015-16': 'float',
           '2016-17': 'float',
           '2017-18': 'float',
           '2018-19': 'float',
           '2019-20': 'float',
           '5-Year % Change': 'float'
         }
        )
    )


df_g1.info()

df_g1.to_csv('data/geneseo_6yr_graduation_rates.csv', 
             index = False)

# %%




