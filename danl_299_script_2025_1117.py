#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 17:24:56 2025

@author: bchoe
"""



# %% 
# =============================================================================
# Python Selenium
# =============================================================================
# Import the necessary modules from the Selenium package
import pandas as pd
import os  

from selenium import webdriver  # Main module to control the browser
from selenium.webdriver.common.by import By  # Helps locate elements on the webpage
from selenium.webdriver.chrome.options import Options  # Allows setting browser options


# Set the working directory path
wd_path = '/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/' # Do not choose your personal website folder
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory


# Create an instance of Chrome options
options = Options()
options.add_argument("window-size=1400,1200")  # Set the browser window size to 1400x1200

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation

# Now you can use 'driver' to control the Chrome browser
url = 'https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php'
driver.get(url)


# find out how many rows and columns are in this table
# number of rows
tbody = driver.find_element(By.TAG_NAME, 'tbody')
trows = tbody.find_elements(By.TAG_NAME, 'tr')
len(trows)

# number of columns
tcols = driver.find_elements(By.TAG_NAME, 'th')
len(tcols)




df = pd.DataFrame()
for item in range(1, len(trows) + 1):
    
    xpath_mon_yr = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[1]'
    xpath_retail_price = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[2]'
    xpath_refining = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[3]'
    xpath_dist_mkt = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[4]'
    xpath_tax = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[5]'
    xpath_crude_oil = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item}]/td[6]'
    
    mon_yr = driver.find_element(By.XPATH, xpath_mon_yr).text
    retail_price = driver.find_element(By.XPATH, xpath_retail_price).text
    refining = driver.find_element(By.XPATH, xpath_refining).text
    dist_mkt = driver.find_element(By.XPATH, xpath_dist_mkt).text
    tax = driver.find_element(By.XPATH, xpath_tax).text
    crude_oil = driver.find_element(By.XPATH, xpath_crude_oil).text
    
    lst_row = [mon_yr, retail_price, refining, dist_mkt, tax, crude_oil]
    obs = pd.DataFrame( [lst_row] )
    
    df = pd.concat([df, obs], ignore_index=True)


df.columns
df.columns = [ 'mon_yr', 'retail_price', 'refining', 'dist_mkt', 'tax', 'crude_oil' ]

df.info()
# WebElement's text data is always string.

df.to_csv('data/eia_2025_1117.csv', index = False)




# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[1]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[2]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[3]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[4]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[5]
# /html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[6]


# collect column names and store them in a list using for-loop

# list's append() method
# lst = []
# type(lst)

# lst.append("a")
# lst.append("b")
# lst.append("c")


for i in range(1, 10):
    print(i)


col_lst = [] # list of the column names
for col in range(1, len(tcols) + 1):
    xpath_col = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/thead/tr/th[{col}]'
    col_name = driver.find_element(By.XPATH, xpath_col).text
    col_lst.append(col_name)



df.columns = col_lst
df.to_csv('data/eia_w_official_colnames_2025_1117.csv', index = False)


# %% 
# =============================================================================
# Nested for-loop
# =============================================================================


# for item_row in range(1, len(trows) + 1):
    
#     for item_col in range(1, len(tcols) + 1):
    
#         xpath_data = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{item_row}]/td[{item_col}]'
        
#         print(xpath_data)



df = pd.DataFrame()
for row in range(1, len(trows) + 1):
    
    obs = []
    for col in range(1, len(tcols) + 1):
        xpath_data = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{row}]/td[{col}]'
        data = driver.find_element(By.XPATH, xpath_data).text
        obs.append(data)
    
    obs = pd.DataFrame( [obs] )
    df = pd.concat([df, obs], ignore_index=True)


df.columns = [ 'mon_yr', 'retail_price', 'refining', 'dist_mkt', 'tax', 'crude_oil' ]

df.info()
# WebElement's text data is always string.

df.to_csv('data/eia_from_nested_loop_2025_1117.csv', index = False)









# %%
# =============================================================================
# this section is blank
# =============================================================================


