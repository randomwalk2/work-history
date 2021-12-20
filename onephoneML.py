#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import re
columnNames = ['first_name','last_name','title','first_name_alt','last_name_alt','company','industry','address','city','state','zip','phone number']

df = pd.read_csv("/Users/jeremiahmcleod/Downloads/ML Valley Direct Buying _ Proj 1 - Camp 4_5 of 12 - 300 Contacts Managed (contact list.4) - Copy of ML Form  (4).csv")                    # read csv file from folder_location/filename
df_orig = df                                                                                     # save copy of created df (dataframe) as df_orig
df.reset_index()                                                                                 # sets numbers as index
df.columns = columnNames                                                                         # references names from column_names field
df = df[df['phone number'].notna()]                                                              # set df to df(without nan phone numbers)
df = df.drop_duplicates(['phone number','first_name','company'], keep='last')          # drop duplicates based on specified columns, try to use atleast 3']
df['phone number'] = df['phone number'].astype(str).astype(str) 
df['phone number'] = [re.sub("[^0-9,'']","", str(x)) for x in df['phone number']]                # delete anything other than 0-9 and replaces with closed space for every instance in phone_number column 
df['phone number'] = df['phone number'].astype(str).astype(str)                                  # ensure dtype is string to perform next line
df['phone number'] = [s.lstrip("1") for s in df['phone number']]                                   # strip first number from phone number if it is a 1
df['phone number'] = df['phone number'].str[:10]                                                 # phone number is first 10 digits
#df['phone number'] = df['phone number'].astype(int).astype(str)                                 # 
df['phone number'] = df['phone number'].astype(int).astype(int)                                  # ensure code worked and phone_number col is colored indicating (int)
df = df.drop(df[df['phone number'] < 1000000000].index)                                            # drop phone numbers less that 10 digits
df['phone number'] = df['phone number'].astype(int).astype(int)                                  # insure again integer
#4  Upload this file to dnc for compliance scan
df.to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/compliancescan103.csv")                 # output file

#%%
denied = ['2018', '2019','2020',';;;W',';;W','Litigator']                                        # define denied leads
Vonage = [';;;W',';;W']                                                                          # wir leads defined as vonage
df43 = pd.read_csv(r"/Users/jeremiahmcleod/Downloads/compliancescan103_1206278529/detailed.csv") # import dnc downloaded detailed file
df43 = df43.iloc[1:]                                                                             # start file on second line (0 = first line)
df43.columns = ['phone number','result_code', 'reserved', 'reason', 'state', 'country', 'city',
                'carrier_info', 'new_reassigned', 'tz_code', 'calling_window', 'utcoffset',
                'dnc_today', 'calltimereset', 'ebr_type', 'wireless', 'line_type']
df430 = df43[['phone number','reason']]                                                          # 
df431 = df.merge(df430, left_on='phone number', right_on='phone number')                         # 
df431 = df431.drop_duplicates(['phone number','first_name','company'],keep='last')             # 
df431['reason'] = df431['reason'].astype(str).astype(str)                                        # 
df19 = df431[df431['reason'].str.contains('|'.join(denied))]                                     # 
df25 = df431[df431['reason'].str.contains('|'.join(Vonage))]                                     # 
df431 = df431[~df431.reason.str.contains('|'.join(denied))]                                      # 
df431 = df431.sample(frac=1)
df431[0:300].to_csv("/Users/jeremiahmcleod/Desktop/PereusMarketing/vanillasoft_upload.csv")      # 
writer = pd.ExcelWriter('/Users/jeremiahmcleod/Desktop/PereusMarketing/marketing_list.xlsx', engine='xlsxwriter')
df_orig.to_excel(writer, sheet_name='original_ml')                                               # 
df431.to_excel(writer, sheet_name='approved_leads')                                              #                                                                            # 
del df431['reason']                                                                              # 
df431[0:100].to_excel(writer, sheet_name='leads4camp')                                           # 
df431[101:].to_excel(writer,sheet_name='use_next_camp')                                          # 
df19.to_excel(writer,sheet_name='denied_leads')                                                  # 
df25.to_excel(writer,sheet_name='vonage_leads')                                                  # 
writer.save()                                                                                    # 



#%%
import lux
import pandas as pd