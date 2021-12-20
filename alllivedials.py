#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:12:12 2020

@author: jeremiahmcleod
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:21:51 2020

@author: jeremiahmcleod
"""


#%% link
#https://docs.google.com/spreadsheets/d/1b5hBs7-Ao8MCEC4_KznmJaPvTyYeivmO-V9mWrjUp04/edit#gid=670628349
#%% import libraries
import datetime
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


#%% sheet id is the long string of numbers and letters insie the http link:
# pan between multiple links by commenting out a line with a #
#sheet_id'1b5hBs7-Ao8MCEC4_KznmJaPvTyYeivmO-V9mWrjUp04'
sheet_id = '1b5hBs7-Ao8MCEC4_KznmJaPvTyYeivmO-V9mWrjUp04'
#sheet_id = '16acnfMeLW7e_w1nJVtCNOc-Xq3FjS2CgxZS7gGu_zN4'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
#%% name columns
df.columns = ['camp1','del1','del2','del3','del4','del5','dialsmade','del7','del8','del9','del10','camp','email','phone','status','time','sdr','del11','del12'
              ,'del13','del14','del15','del16','del17','del18','del19','del20','del21','del22','del23']
#del df['del1']

#%% delete unneeded columns
del df['del1']
del df['camp1']
del df['del3']
del df['del2']
del df['del4']
del df['del5']
del df['dialsmade']
del df['del7']
del df['del8']
del df['del9']
del df['del10']
del df['del11']
del df['del12']
del df['del13']
del df['del14']
del df['del15']
del df['del16']
del df['del17']
del df['del18']
del df['del19']
del df['del20']
del df['del21']
del df['del22']
del df['del23']
#%% check head, delete excel header
df = df.iloc[1:]
print(df.head())
#%% dataframe with qualifying statuses
df15 = df[(df.status == 'DM Interested - Appt. Set') | 
         (df.status == 'DM Interested - Nurture') | 
         (df.status == 'Dm Interested - Warm Lead')]
#%%
df15['camp'] = df15['camp'].astype(str).astype(str)
df15.sdr = df15['sdr'].astype(str).astype(str)
df15.status = df15['status'].astype(str).astype(str)
#%%
df189 = df15.groupby(['camp','sdr']).size().sort_values().reset_index()
df189.columns = ['camp','sdr','score']
scores = str(df189.score)
names = str(df189.sdr)
camp = str(df189.camp)


#%%
df777 = df189.groupby(['camp','sdr']).sum()
df777.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/topsdr.csv")
df777 = df777.reset_index()
df778 = df777['camp'].astype(str).astype(str)
df777.sdr = df777['sdr'].astype(str).astype(str)
df778.reset_index()
df778.columns = ['camp']
df778 = df778['camp'].astype(str).astype(str)
#%%
df778 = df778.drop_duplicates()
#%%
df777.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/bloom.csv")
#%%
for column in df777[['camp','sdr']]:
    columnSeriesObj = df777['score']
    print('Column Name :', column)
    print('Column Contents:', columnSeriesObj.values)
#%%
for i, j in df777.iterrows():
    print(i,j)
    print()

#%%

for i in df777.itertuples():
    print(i)
#%%
print("The top SHP SDRs for " + camp + "are: \n" +names + "|* The matching scores: \n" + scores + "|The best time to call is")


#%%
for camp in df.camp:
    df5 = pd.value_counts(df15.sdr)

#%%
df0 = df.drop_duplicates(subset=['full_name','phone_number'],keep='last')

df0.to_csv('/Users/jeremiahmcleod/Desktop/PereusMarketing/lastcall.csv')