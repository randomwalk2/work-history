#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 08:02:38 2021

@author: jeremiahmcleod
"""

from pprint import pprint
import datetime
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.marketwatch.com/tools/screener/short-interest"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0'}
#Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:71.0) Gecko/20100101 Firefox/71.0
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')

dfs = {}

screener_tables = soup.find_all('div', {'class': 'element element--table table--fixed screener-table'})

xlsxwriter = pd.ExcelWriter('After Hour Screener Tables.xlsx')

for screener_table in screener_tables:
    screener_name = screener_table.h2.text
    screener_table = screener_table.find('table')
    df = pd.read_html(str(screener_table))[0]
    df['Symbol Symbol'] = df['Symbol Symbol'].str.replace(
    r'\b(.+)(\s+\1)+\b',
    r'\1')

    df.rename({'Symbol Symbol': 'Symbol'}, axis=1)
    dfs[screener_name] = df
    df.to_excel(xlsxwriter, sheet_name=screener_name, index=False)

xlsxwriter.save()

#%%
from pprint import pprint
import datetime
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.marketwatch.com/tools/screener/after-hours"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0'}
#Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:71.0) Gecko/20100101 Firefox/71.0
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')


dfs = {}

screener_tables = soup.find_all('div', {'class': 'element element--table table--fixed screener-table'})

xlsxwriter = pd.ExcelWriter('After Hour Screener Tables.xlsx')

for screener_table in screener_tables:
    screener_name = screener_table.h2.text
    screener_table = screener_table.find('table')
    df = pd.read_html(str(screener_table))[0]
    df['Symbol Symbol'] = df['Symbol Symbol'].str.replace(
    r'\b(.+)(\s+\1)+\b',
    r'\1')

    df.rename({'Symbol Symbol': 'Symbol'}, axis=1)
    dfs[screener_name] = df
    df.to_excel(xlsxwriter, sheet_name=screener_name, index=False)

xlsxwriter.save()
