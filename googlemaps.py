#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:09:35 2020

@author: jeremiahmcleod
"""


import pandas as pd
df3 = pd.read_csv('/Users/jeremiahmcleod/Desktop/PereusMarketing/sddr.csv')
df3.columns = ['camp','user','login_time','call_duration','talk_time','appt',
             'warm','nurture','survey','total','dm_conv','dials','lead_per_hr',
             'dm_hr','appts_hr','dials_hr','asr','dcr','conv_appt','talk_time1','talk_time2','app100']

sheet_id = '1b5hBs7-Ao8MCEC4_KznmJaPvTyYeivmO-V9mWrjUp04'
df4 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
df4 = df4.iloc[1:]
df4.columns = ['camp','type','status','tot_dials','remaining_dials','dials_made',
               'conversations','appts','del9','del10','del11','del12','del13','del14',
               'del15','del16','del17','del18','del19']
del df4['del9']
del df4['del10']
del df4['del11']
del df4['del12']
del df4['del13']
del df4['del14']
del df4['del15']
del df4['del16']
del df4['del17']
del df4['del18']
df4 = df4.loc[df4['status'] == 'Live']

#%%
