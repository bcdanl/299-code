#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:35:35 2025

@author: bchoe
"""


# %% 
# =============================================================================
# Python Selenium
# =============================================================================
# Import the necessary modules from the Selenium package
from selenium import webdriver  # Main module to control the browser
from selenium.webdriver.common.by import By  # Helps locate elements on the webpage
from selenium.webdriver.chrome.options import Options  # Allows setting browser options

# Create an instance of Chrome options
options = Options()
options.add_argument("window-size=1400,1200")  # Set the browser window size to 1400x1200

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation

# Now you can use 'driver' to control the Chrome browser
form_url = "https://qavbox.github.io/demo/webtable/"
driver.get(form_url)
# driver.close()
# driver.quit()

# By.ID

form = driver.find_element(By.ID, "form1")
form.text

btn = driver.find_element(By.CLASS_NAME, "homebtn")


type(btn)

btn.click()
driver.back()


btn_2 = driver.find_element(By.NAME, "home")
btn_2.click()
driver.back()

btn_3 = driver.find_element(By.CSS_SELECTOR, "body > div > a > input")
btn_3.click()


table01 = driver.find_element(By.ID, "table01")
table01.text

th01 = table01.find_element(By.TAG_NAME, "thead")
th01.text

selenium_link = driver.find_element(By.LINK_TEXT, "Selenium")
selenium_link.click()
driver.back()


qav_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "qav")
qav_links
len(qav_links)

qav_links[0]
qav_links[1]

qav_links[0].click()
driver.back()
qav_links[1].click()
driver.back()

qav_link = driver.find_element(By.PARTIAL_LINK_TEXT, "qav")
qav_link.click()

xpath = '//*[@id="table02"]/thead/tr/th[1]'
full_xpath = '/html/body/form/fieldset/div/div/table/thead/tr/th[1]'



table_row = driver.find_element(By.TAG_NAME, 'tr')
table_row.text

table_rows = driver.find_elements(By.TAG_NAME, 'tr')
len(table_rows) # 60 tr tags



xpath = '//*[@id="table02"]/tbody/tr[1]/td[1]'
tiger = driver.find_element(By.XPATH, xpath)
tiger.text



xpath = '//*[@id="table02"]/tbody/tr[2]/td[1]'
gw = driver.find_element(By.XPATH, xpath)
gw.text


xpath = '//*[@id="table02"]/tbody/tr[3]/td[1]'
ac = driver.find_element(By.XPATH, xpath)
ac.text



selenium_link = driver.find_element(By.LINK_TEXT, "Selenium")
selenium_link.get_attribute('href')


btn = driver.find_element(By.XPATH, '/html/body/div/a/input')

'//*[@id="btn"]'
driver.find_element(By.XPATH, '//*[@id="btn"]').get_attribute('value')


# %%
# Classwork 9
# Question 1

url = 'https://www.eia.gov/petroleum/gasdiesel/gaspump_hist.php'
driver.get(url)


# data concatenation review
import pandas as pd
df1 = pd.read_csv('https://bcdanl.github.io/data/concat_1.csv')
df2 = pd.read_csv('https://bcdanl.github.io/data/concat_2.csv')

df0 = pd.DataFrame()
df0 = df1
df0 = pd.concat([df0, df2])


for i in range(1, 10):
    xpath = f'/html/body/div[1]/div[2]/div/div[4]/div/div[1]/div/table/tbody/tr[{ i }]/td[1]'
    print(xpath)

# find out how many rows and columns are in this table
# number of rows
tbody = driver.find_element(By.TAG_NAME, 'tbody')
trows = tbody.find_elements(By.TAG_NAME, 'tr')
len(trows)

# number of columns
tcols = driver.find_elements(By.TAG_NAME, 'th')
len(tcols)

# xpaths for Mon-yr's first 3 rows:
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[1]/td[1]
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[2]/td[1]
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[3]/td[1]
# ....
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[309]/td[1]

# xpaths for retail price's first 3 rows:

# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[1]/td[2]
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[2]/td[2]
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[3]/td[2]


# xpaths for crude oil 's first 3 rows:

# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[1]/td[6]
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[2]/td[6]
# /html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[3]/td[6]


# list(range(1, len(trows)))


# below gives a DataFrame with a single row
# pd.DataFrame( [ LIST ] )
obs = pd.DataFrame( [ ["a", "b", "c", "d"] ] )


df = pd.DataFrame()
for item in range(1, len(trows) + 1):
    
    xpath_mon_yr = f'/html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[{item}]/td[1]'
    xpath_retail_price = f'/html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[{item}]/td[2]'
    xpath_refining = f'/html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[{item}]/td[3]'
    xpath_dist_mkt = f'/html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[{item}]/td[4]'
    xpath_tax = f'/html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[{item}]/td[5]'
    xpath_crude_oil = f'/html/body/div[1]/div[2]/div/div[5]/div/div[1]/div/table/tbody/tr[{item}]/td[6]'    
    
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


df.to_csv('/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/data/eia_2025_1112.csv', index = False)











