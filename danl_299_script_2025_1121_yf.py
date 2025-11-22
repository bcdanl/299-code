#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 16:57:59 2025

@author: bchoe
"""

import pandas as pd
from io import StringIO
from datetime import datetime, timezone
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 1. Chrome options
options = Options()
options.add_argument("window-size=1400,1200")
# (Optional) pretend to be a normal browser
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/129.0.0.0 Safari/537.36"
)

# 2. Start driver
driver = webdriver.Chrome(options=options)

# Set a page load timeout (in seconds)
driver.set_page_load_timeout(60)

url = "https://finance.yahoo.com/quote/MSFT/history/?p=MSFT&period1=1704067200&period2=1761868800"


# 3. Load the page (can raise timeout)
driver.get(url)

# Optional: small random delay to let JS settle
time.sleep(random.uniform(2, 4))

# 4. Wait for the table to appear
wait = WebDriverWait(driver, 40)  # increased from 20 -> 40
table = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

table_html = table.get_attribute("outerHTML")

# 5. Parse the HTML table into a pandas DataFrame
df = pd.read_html(StringIO(table_html))[0]


