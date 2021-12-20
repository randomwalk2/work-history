#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:48:28 2020

@author: jeremiahmcleod
"""

#%% link
#https://docs.google.com/spreadsheets/d/1b5hBs7-Ao8MCEC4_KznmJaPvTyYeivmO-V9mWrjUp04/edit#gid=670628349
#%% import libraries
import pandas as pd
# sheet id is the long string of numbers and letters insie the http link:
sheet_id = '1b5hBs7-Ao8MCEC4_KznmJaPvTyYeivmO-V9mWrjUp04'
df0 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
df0.columns = ['camp1','del1','del2','del3','del4','del5','dialsmade','del7','del8','del9','del10','camp','email','phone','status','time','sdr','del11','del12'
              ,'del13','del14','del15','del16','del17','del18','del19','del20','del21','del22','del23']
df0 = df0.iloc[1:]
del df0['del1']
del df0['camp1']
del df0['del3']
del df0['del2']
del df0['del4']
del df0['del5']
del df0['dialsmade']
del df0['del7']
del df0['del8']
del df0['del9']
del df0['del10']
del df0['del11']
del df0['del12']
del df0['del13']
del df0['del14']
del df0['del15']
del df0['del16']
del df0['del17']
del df0['del18']
del df0['del19']
del df0['del20']
del df0['del21']
del df0['del22']
del df0['del23']

#%%
df15 = df0[(df0.status == 'DM Interested - Appt. Set') | 
         (df0.status == 'DM Interested - Nurture') | 
         (df0.status == 'Dm Interested - Warm Lead')]
df15.camp = df15['camp'].astype(str).astype(str)
df15.sdr = df15['sdr'].astype(str).astype(str)
df15.status = df15['status'].astype(str).astype(str)
df15 = df15.groupby('camp')['sdr'].value_counts()

#%%
df15 = df15.reset_index()
df15.columns = ['camp','sdr','score']

#%%
df16 = df15.to_frame()
df16.columns = ['count']
df17 = pd.concat([df15,df16], axis=1)

#%%

df189.columns = ['camp','sdr','score']
scores = str(df189.score)
names = str(df189.sdr)
camp = str(df189.camp)


#%%
df777 = df189.reset_index()

df777.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/topsdr.csv")
#%%
df778 = df778.drop_duplicates()
#%%
df777.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/bloom.csv")

#%%
rankk = df15.groupby('camp')['sdr','score'].rank(ascending=True,method='first')
rankk.name = 'rank'
rankked = pd.concat([df15,rankk],axis=1)
#ranked = ranked.groupby(ranked['camp'])

#%%
ranks = df777.groupby('camp')['score','sdr'].rank(ascending=True,method='first')
ranks.name = 'rank'
ranked = pd.concat([df777,ranks],axis=1)
#ranked = ranked.groupby(ranked['camp'])
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