#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:35:31 2020

@author: jeremiahmcleod
"""
#call tracker data: best time to call '#camp' template
#%% link
https://docs.google.com/spreadsheets/d/16acnfMeLW7e_w1nJVtCNOc-Xq3FjS2CgxZS7gGu_zN4/edit#gid=0

https://docs.google.com/spreadsheets/d/1SfQaddB1Yjai0hXQ6FLSjwjKLmku1m1A48-JTCml7qc/edit#gid=0
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

#%% assign column names within df, remove first row, 
#  convert object to int, delete unneeded columns
df.columns = ['delete1','contact_ID', 'project_id','project_name','company',
              'contact_website','email','address','full_name','phone_number',
              'alt_phone','result_count','lead_status','call_date_time',
              'user_name','comment','call_hist','iss_details','project_mgmt'
              ]
df = df.iloc[1:]

del df['delete1']
del df['contact_ID']
del df['project_id']
del df['contact_website']
del df['alt_phone']
del df['iss_details']
del df['project_mgmt']


#%% create a df of qualifying lead_status
df9 = df[(df.lead_status == 'DM Interested - Appt. Set') | 
         (df.lead_status == 'DM Interested - Nurture') | 
         (df.lead_status == 'Dm Interested - Warm Lead')]
camp = df.at[3,'project_name']

#%% separate date and time from df
df1 = pd.DataFrame(df9.call_date_time.str.split(' ',1).tolist(),
                  columns = ['Date','Time'])
df1.Hour = df1['Hour'].astype(str).astype(int)
#%% df representing hour(block) of qualifying lead_status
df2 = pd.DataFrame(df1.Time.str.split(':',2).tolist(),
                  columns = ['Hour','Minute','Second'])

#%% Top Qualifying SDR's this Campaign, distribution
df9.user_name = df9['user_name'].astype(str).astype(str)
df5 = pd.value_counts(df9.user_name)
df5 = df5.reset_index()
df5.columns = ['sdr', 'tally']
names = str(df5.sdr)
scores = str(df5.tally)
df6 = pd.value_counts(df2.Hour)
df6 = df6.reset_index()
df6.columns = ['hour','count']
df6.sort_values(by=['hour'])
df6.hour = df6['hour'].astype(str).astype(int)

#%% Times Qualifying Leads are Set
plt.scatter(df6["hour"],df6["count"])
plt.title("Qualifying Leads " + camp)
plt.xlabel('Time(24hr)')
plt.ylabel('Total Qualifying Leads')

#%% Top Callers for #camp

print("The top SHP SDRs for " + camp + " are: \n" + names + "|* The matching scores:\n" + scores + "| The best time to call has been Afternoon")
