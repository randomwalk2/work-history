#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:19:11 2020

@author: jeremiahmcleod
"""


#Import Vanillasoft call results for past month.

# First appt set gets 2x multiplier
# Each warm is 1$

import pandas as pd
df = pd.read_csv('/Users/jeremiahmcleod/Downloads/Dashboard_139145_User_11-30-2020_8-50-29_PM.csv')
del df['Project']
#df1 = df.groupby('User',group_keys=True)
appt_total = df['Appt Set'].sum()
warm_total = df['Warm Lead'].sum()
print(appt_total)
print(warm_total)
df = df.groupby(['User']).sum()
df['ASR'] = df['Appt Set'] / df['Dials']
df['elligible'] = df['ASR'] >= .0000125
df2 = df.loc[df['ASR'] >= .0000125]
appt_total = df2['Appt Set'].sum()
print(appt_total)
warm_total = df2['Warm Lead'].sum()
print(warm_total)
df2 = df2.reset_index()
df3 = df2[['User', 'Appt Set','Warm Lead','Nurture','ASR','elligible']]
df3['Bonus'] = df3['Appt Set'] * 5 + df3['Warm Lead'] * 1
df3.to_excel('/Users/jeremiahmcleod/Downloads/october_SDR_bonuses.xlsx')

#%%  trit is from other file, must run that scrip first for now 

df_noz = trit.loc[~((trit['lead_total'] == 0))]
df_noz = df_noz.groupby(['sdr']).count().reset_index()
df_soundboard = df_noz[['camp','sdr']]
df_soundboard.columns = ['sound_board_pts', 'sdr']
df3 = pd.merge(df3,df_soundboard, right_on='sdr', left_on='User')
df3.to_excel('/Users/jeremiahmcleod/Downloads/october_SDR_bonuses.xlsx')
bonus_total = df3['Bonus'].sum()
print(bonus_total)
print(appt_total)