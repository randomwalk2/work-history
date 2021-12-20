#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:30:03 2020

@author: jeremiahmcleod
"""


#shift is number of hours available to schedule
#calls_per_hour = number of calls to schdule per hour working, (account for 1 hr for meetings and script writing)

dict = {}
employee_1 = {"shift": [9,17,0,1.5],                                            # start time, endtime, time-zone (3=T=WTZ),(0=CT), time restriction
              "calls_per_hour": 22,                                             # call efficiency of SDR
              "days_to_schedule": "MTWTH"                                       # search for th, before t
              }   
print(employee_1["shift"][0])
calling_hours = (employee_1["shift"][1]-employee_1["shift"][0] -employee_1["shift"][3])
dials_to_schedule = calling_hours * employee_1["calls_per_hour"]
start_time = employee_1["shift"][0] + employee_1["shift"][2]
                    # start time adds a time zone to beginning start time
#%% can make new dict for each day of week if schedules change beteween days (otherwise use days code)
keys = ['employee_1','shift','DPH','days']
DICTo = {'employee_1': {'shift': [9,17,0,1.5], 'DPH': 22,'days':'MTWTHF'},      # start time, endtime, time-zone (3=T=WTZ),(0=CT), time restriction
         'employee_2': {'shift': [14,22,0,1.5], 'DPH': 14,'days':'MTWTHF'},
         'employee_3': {'shift': [8,13,0,1.5], 'DPH': 18,'days':'MTWTHF'},
         'employee_4': {'shift': [9,10,0,], 'DPH': 20,'days':'MTTHF'}}

sas['hours_employee 1'] = (DICTo['employee_1']["shift"][1] - DICTo['employee_1']["shift"][0]).astype(int).astype(int)
#%%
import pandas as pd
sas = DICTo['employee_1']["shift"]
df = pd.DataFrame(DICTo).reset_index()
#%%
sam = []
for d in DICTo:
    for k in DICTo[d]["shift"]:
        print((((DICTo[d]["shift"][1])-(DICTo[d]["shift"][0])),d))
#        print(d, (DICTo[k]["shift"][1])-(DICTo[k]["shift"][0]), k)

#%%

sam = []
for i in DICTo:
    for d,k in DICTo[d][k]:
        print((((DICTo[i]["shift"][1])-(DICTo[i]["shift"][0])),i))
#        print(d, (DICTo[k]["shift"][1])-(DICTo[k]["shift"][0]), k)
#%%
sam = []
sam['cheer'] = ((DICTo[i]["shift"][1])-(DICTo[i]["shift"][0]))
#%%
for k in DICTo.values():
    for d in k["shift"]:
        print(((d, DICTo[values]["shift"][1])-DICTo[values]["shift"][0]))
#%%
d = {}
for i in DICTo:
    dials[i] = DICTo[i]['shift'][1] - DICTo[i]['shift'][0]


#%%dials_to_schedule = 0
for key in DICTo.keys():
    if key == (DICTo[key]["shift"][0]):
        print(key)

    
#%%
print(DICTo.keys())
 
# create camp calling window column to match start/end time for sdr scheduling (client preference and time zone)
# each camp has block schedulable per sdr (based of speed of calls, possibly updateable)
# summary best time to call each camp