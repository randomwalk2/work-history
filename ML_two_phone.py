#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:34:42 2020

@author: jeremiahmcleod
"""
#instructions: (do not change layout)
# ML phone number must be separated from ext., if country code other than +1 is used - delete row before importing. 


#1  Specify column names in line #23 in exact order as appears on csv
#2  Change campaign name on line #24. Change filepath line #25
#   Change filepath to write file on line #45
#3  Shift+enter to execute cell. this outputs dnc ready file.

#useable column names
# 'first_name', 'last_name', 'title', 'company', 'address_1', 'phone_number'
# 'alt_phone', 'city', 'state', 'zip', 'country', 'linkedin', 'website', 
# 'phone_number_ext', 'email', 'industry' 'full_name'
import re
import pandas as pd
columnNames = ['first_name','last_name','phone_number','alt_phone','email','address 1','city','state','zip']
campaign = 'ML | Insurance You Keep (IYK) | Proj 1 Camp 8b - Final Camp'
salesAssociate = 'Chris Jones'
df = pd.read_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/IYK.csv")
df_orig = df
df.reset_index()
df.columns = columnNames
df = df.drop_duplicates(['email','phone_number','alt_phone'],keep='last')
df=df.dropna(subset=['phone_number','alt_phone'])
df1 = df[df['alt_phone'].notna()]
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
#5  Change filepath to extracted(detailed) file from dnc compliance scan line #51
#6  Change filepath lines #63
#7  Change filepath lines #64
#8  How many Leads? Specify Line #69 place a '#' at start of line 70 if all leads used
#9  Shift+Enter
#wiR = ['AZ','LA','NJ','TX','WY','Arizona','Louisana','New Jersey','Texas','Wyoming']
#searchfor = ['2018', '2019','2020',';;;W',';;W','Litigator']
searchfor = ['2018', '2019','2020','Litigator']
df43 = pd.read_csv(r"/Users/jeremiahmcleod/Desktop/PereusMarketing/detailed_phone.csv")
df43 = df43.iloc[1:]
df437 = pd.read_csv(r"/Users/jeremiahmcleod/Desktop/PereusMarketing/detailed_alt.csv")
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
df431 = df.merge(df430, left_on='phone_number', right_on='phone_number')
#df431 = df.merge(df430, how='outer')

df1['alt_phone'] = df1['alt_phone'].astype(int).astype(int)
df434 = df1.merge(df433, left_on='alt_phone', right_on='alt_phone')
#df434 = df1.merge(df433, how='outer')


df431['reason'] = df431['reason'].astype(str).astype(str)
df434['reason_alt'] = df434['reason_alt'].astype(str).astype(str)



df19 = df431[df431['reason'].str.contains('|'.join(searchfor))]
df434['reason_alt'] = df434['reason_alt'].astype(str).astype(str)
df20 = df434[df434['reason_alt'].str.contains('|'.join(searchfor))]
df431 = df431[~df431.reason.str.contains('|'.join(searchfor))]
df434 = df434[~df434.reason_alt.str.contains('|'.join(searchfor))]
df431.insert(loc=0,column='approval_',value='Approved')
df434.insert(loc=0,column='approval_alt',value='Approved')
df431.insert(loc=0,column='campaign',value=campaign)
df434.insert(loc=0,column='campaign',value=campaign)
df435 = df431.merge(df434,how='outer')
#df435 = df431.merge(df434,left_on=['first_name','last_name','address 1','city','state','zip'],right_on=['first_name','last_name','address 1','city','state','zip'])
del df435['approval_alt']
df435.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/vanillasoft_upload.csv")
writer = pd.ExcelWriter('/Users/jeremiahmcleod/Desktop/PereusMarketing/marketing_list.xlsx', engine='xlsxwriter')
df_orig.to_excel(writer, sheet_name='original_ml')
df435.to_excel(writer, sheet_name='approved_leads')
del df435['approval_']
del df435['reason']
del df435['reason_alt']
#del df435['approval_alt']

df435[0:].to_excel(writer, sheet_name='leads4camp')
#df435[101:].to_excel(writer,sheet_name='use_next_camp')
df19.to_excel(writer,sheet_name='denied_leads_phone')
df20.to_excel(writer,sheet_name='denied_leads_alt_phone')
writer.save()

#10 file is saved, upload to google sheets and then vanillasoft

#%% copy contents to line #36 if phone_number_ext column if used
df['phone_number_ext'] = [re.sub("[^0-9,''+]","", str(x)) for x in df['phone_number_ext']]


#%% check if email is valid (beta) - does not currently work
df['email'] = [re.sub("[A-Za-z0-9._+]+@[A-Za-z]+.(com|org|edu|net)"," ", 
                      str(x)) for x in df['email']]


