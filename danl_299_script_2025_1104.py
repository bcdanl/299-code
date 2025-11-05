#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 14:39:09 2025

@author: bchoe
"""

import pandas as pd


df1 = pd.read_csv('https://bcdanl.github.io/data/concat_1.csv')
df2 = pd.read_csv('https://bcdanl.github.io/data/concat_2.csv')
df3 = pd.read_csv('https://bcdanl.github.io/data/concat_3.csv')

df1.index
df1.columns

row_concat = pd.concat([df1, df2, df3])



col_concat = pd.concat([df1, df2, df3], axis = "columns")



pd.concat([df1, df2, df3], axis = "columns", ignore_index = True)  

pd.concat([df1, df2, df3], ignore_index = True)  

# create a new row of data
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])

new_row_series

df1

pd.concat([df1, new_row_series])

# attempt to add the new row to a DataFrame
df = pd.concat([df1, new_row_series])
df

#     A   B   C   D
# 0  a0  b0  c0  d0
# 1  a1  b1  c1  d1
# 2  a2  b2  c2  d2
# 3  a3  b3  c3  d3
# 4  n1  n2  n3  n4


new_row_df = pd.DataFrame(
  # note the double brackets to create a "row" of data
  data =[ ["n1", "n2", "n3", "n4"] ],
  columns = df1.columns,
)

df = pd.concat( [df1, new_row_df] )
df




pd.concat([df1, new_row_series])

new_row_series
pd.concat([df1, new_row_series], axis = 1)
pd.concat([df1, new_row_series], axis = "columns")



# %%

student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})



student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})




# Write a Pandas code to concatenate the two given DataFrames along rows.

student_rows = pd.concat([student_data1, student_data2])
student_rows

# Write a Pandas code to concatenate the two given DataFrames along columns.

student_cols = pd.concat([student_data1, student_data2], axis = 1)
student_cols



s6 = pd.Series(['S6', 'Scarlette Fisher', 205], 
               index=['student_id', 'name', 'marks'])

s6

student_data1

df_s6 = pd.DataFrame(s6)
df_s6 = df_s6.T
df_s6

student_data_added = pd.concat([student_data1, df_s6])





