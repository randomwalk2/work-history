#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:41:44 2020

@author: jeremiahmcleod
"""

import re
import pandas as pd
columnNames = ['company','first_name','last_name','title','email','alt_phone','phone_number','portal link',
               'calendly','sales representative']
campaign = 'edtech'
#salesAssociate = 'Chris Jones'
df = pd.read_csv("/Users/jeremiahmcleod/Downloads/wipfli.csv")
df_orig = df
df.reset_index()
df.columns = columnNames
df = df.drop_duplicates(['first_name','last_name','email','company'],keep='last')
df1 = df[df['alt_phone'].notna()]
df=df.dropna(subset=['phone_number'])

#df = df[df['phone_number'].notna()]
df['phone_number'] = [re.sub("[^0-9,'']","", str(x)) for x in df['phone_number']]
df1['alt_phone'] = [re.sub("[^0-9,'']","", str(x)) for x in df1['alt_phone']]

df1['alt_phone'] = df1['alt_phone'].astype(str).astype(int)
#df1 = df1.drop(df1[df1.alt_phone < 1000000000].index)
del df1['phone_number']
del df['alt_phone']

df['phone_number'] = [re.sub("[^0-9,'']","", str(x)) for x in df['phone_number']]
df['phone_number'] = df['phone_number'].astype(str).astype(str)
df['phone_number'] = [s.lstrip("1") for s in df.phone_number]
df['phone_number'] = df['phone_number'].astype(str).astype(str)
df['phone_number'] = df['phone_number'].str[:10]
df['phone_number'] = df['phone_number'].astype(str).astype(int)
df['phone_number'] = df['phone_number'].astype(int).astype(int)
df['phone_number'] = df['phone_number'].astype(int).astype(int)
df1['alt_phone'] = [re.sub("[^0-9,'']","", str(x)) for x in df1['alt_phone']]
df1['alt_phone'] = df1['alt_phone'].astype(str).astype(str)
df1['alt_phone'] = [s.lstrip("1") for s in df1.alt_phone]
df1['alt_phone'] = df1['alt_phone'].astype(str).astype(str)
df1['alt_phone'] = df1['alt_phone'].str[:10]
#df1['alt_phone'] = df1['alt_phone'].astype(int).astype(int)
df['phone_number'] = df['phone_number'].astype(int).astype(int)
df1['alt_phone'] = df1['alt_phone'].astype(int).astype(int)

#4  Upload this file to dnc for compliance scan
df.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/compliance_phone.csv")
df1.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/compliance_alt.csv")

#%%

searchfor = ['2018', '2019','2020',';;;W',';;W','Litigator']
vonage = [';;W',';;;W']
df43 = pd.read_csv(r"/Users/jeremiahmcleod/Downloads/compliance_phone_1174740090/detailed.csv")
df43 = df43.iloc[1:]
df437 = pd.read_csv(r"/Users/jeremiahmcleod/Downloads/compliance_alt_1174740520/detailed.csv")
df437 = df437.iloc[1:]
##########3 complete after this line
df43.columns = ['phone_number','result_code', 'reserved', 'reason', 'state', 'country', 'city',
                'carrier_info', 'new_reassigned', 'tz_code', 'calling_window', 'utcoffset',
                'dnc_today', 'calltimereset', 'ebr_type', 'wireless', 'line_type']
df437.columns = ['alt_phone','result_code', 'reserved', 'reason_alt', 'state', 'country', 'city',
                'carrier_info', 'new_reassigned', 'tz_code', 'calling_window', 'utcoffset',
                'dnc_today', 'calltimereset', 'ebr_type', 'wireless', 'line_type']
df430 = df43[['phone_number','reason']]
df433 = df437[['alt_phone','reason_alt']]
#df431 = df.merge(df430, left_on='phone_number', right_on='phone_number')
df431 = df.merge(df430, how='outer')

df1['alt_phone'] = df1['alt_phone'].astype(int).astype(int)
df434 = df1.merge(df433, left_on='alt_phone', right_on='alt_phone')
#df434 = df434.drop_duplicates(['first_name','last_name','email'],keep='last')
#df434 = df1.merge(df433, how='outer')


df431['reason'] = df431['reason'].astype(str).astype(str)
df434['reason_alt'] = df434['reason_alt'].astype(str).astype(str)

df19 = df431[df431['reason'].str.contains('|'.join(searchfor))]
df26 = df431[df431['reason'].str.contains('|'.join(vonage))]
df434['reason_alt'] = df434['reason_alt'].astype(str).astype(str)
df20 = df434[df434['reason_alt'].str.contains('|'.join(searchfor))]
df27 = df434[df434['reason_alt'].str.contains('|'.join(vonage))]
df431 = df431[~df431.reason.str.contains('|'.join(searchfor))]
df434 = df434[~df434.reason_alt.str.contains('|'.join(searchfor))]
df431.insert(loc=0,column='approval_',value='Approved')
#df434.insert(loc=0,column='campaign',value=campaign)
#df435 = df431.merge(df434,how ='left', on=['first_name','last_name','city','state','email','company','zip','address','title','industry'])
df435 = df431.merge(df434,how='outer')
df435 = df435.drop_duplicates(['first_name','last_name','email','company','title'])
df435 = df435.groupby('company').head(2)
#df435.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/vanillasoft_upload.csv")
writer = pd.ExcelWriter('/Users/jeremiahmcleod/Desktop/PereusMarketing/marketing_list.xlsx', engine='xlsxwriter')
df_orig.to_excel(writer, sheet_name='original_ml')
df435 = df435.drop_duplicates(['first_name','last_name','company'],keep='last')
df435 = df435.sample(frac=1)
df435.to_excel(writer, sheet_name='approved_leads')
del df435['approval_']
del df435['reason_alt']
#del df435['approval_alt']
#df_vonage = pd.concat([df26,df27])
df435[0:1000].to_excel(writer, sheet_name='leads4camp')
df435[101:].to_excel(writer,sheet_name='use_next_camp')
#df_vonage.to_excel(writer,sheet_name='vonage_leads')
df19.to_excel(writer,sheet_name='denied_leads_phone')
df20.to_excel(writer,sheet_name='denied_leads_alt_phone')

writer.save()

#10 file is saved, upload to google sheets and then vanillasoft

#%% copy contents to line #36 if phone_number_ext column if used
df['phone_number_ext'] = [re.sub("[^0-9,''+]","", str(x)) for x in df['phone_number_ext']]


#%% check if email is valid (beta) - does not currently work
df['email'] = [re.sub("[A-Za-z0-9._+]+@[A-Za-z]+.(com|org|edu|net)"," ", 
                      str(x)) for x in df['email']]


