#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 15:17:27 2025

@author: bchoe
"""


# %% 
# =============================================================================
# Python Selenium
# =============================================================================
# Import the necessary modules from the Selenium package
import pandas as pd
import os  
import time
import random
from io import StringIO

from selenium import webdriver  # Main module to control the browser
from selenium.webdriver.common.by import By  # Helps locate elements on the webpage
from selenium.webdriver.chrome.options import Options  # Allows setting browser options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Set the working directory path
wd_path = '/Users/bchoe/My Drive/suny-geneseo/fall2025/lecture-code/' # Do not choose your personal website folder
os.chdir(wd_path)  # Change the current working directory to wd_path
os.getcwd()  # Retrieve and return the current working directory


# Create an instance of Chrome options
options = Options()
options.add_argument("window-size=1400,1200")  # Set the browser window size to 1400x1200

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)  # Correct implementation


form_url = "https://qavbox.github.io/demo/webtable/"
driver.get(form_url)


elem = driver.find_element(By.XPATH, "element_xpath")



from selenium.common.exceptions import NoSuchElementException
try:
    elem = driver.find_element(By.XPATH, "element_xpath")
    elem.click()
except NoSuchElementException:
    pass

try:
    elem = driver.find_element(By.XPATH, "element_xpath")
    elem.click()
except:
    pass





import time
# time.sleep(3)



# example webpage
url = "https://qavbox.github.io/demo/delay/"
driver.get(url)



driver.find_element(By.XPATH, '//*[@id="one"]/input').click()
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="two"]')
element.text

# //*[@id="oneMore"]/input[1]

driver.find_element(By.XPATH, '//*[@id="oneMore"]/input[1]').click()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
element2 = driver.find_element(By.ID, 'delay')
element2.text


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


element = ( 
  WebDriverWait(driver, 20)  # 20 is timeout in seconds when an expectation is called
  .until(
    EC.presence_of_element_located(
      (By.XPATH, "element_xpath")
      )
    )
) 


# classwork 10 - q1

# Use selenium to get to https://qavbox.github.io/demo/delay/.
# Use selenium to click the button with “Click me!”
# Use selenium to locate the text element that will be displayed after 5 seconds using WebDriverWait with EC.presence_of_element_located.
# Its XPath is '//*[@id="two"]'


driver.find_element(By.XPATH, '//*[@id="one"]/input').click()

element = ( 
  WebDriverWait(driver, 20)  # 20 is timeout in seconds when an expectation is called
  .until(
    EC.presence_of_element_located(
      (By.XPATH, '//*[@id="two"]')
      )
    )
) 

element.text



# %%
# with pd.read_html()


url = 'https://finance.yahoo.com/quote/NVDA/history/?p=NVDA&period1=1672531200&period2=1743379200'
# df_list = pd.read_html(url)


driver.get(url)


# Load content page
url = 'https://finance.yahoo.com/quote/MSFT/history/?p=MSFT&period1=1672531200&period2=1743379200'
driver.get(url)

s = random.uniform(4, 6)

time.sleep( s )  # wait for table to load

# Extract the <table> HTML element
table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute("outerHTML")

# Parse the HTML table into a pandas DataFrame
df = pd.read_html(StringIO(table_html))[0]




# %%
# This section is intendedly left blank.


