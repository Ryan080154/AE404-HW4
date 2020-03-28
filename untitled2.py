# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:11:28 2020

@author: Home
"""

import requests
from bs4 import BeautifulSoup
import re

respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books/")
soup = BeautifulSoup(respond.text,"html.parser")

a_tags = soup.find_all('a')
for url in a_tags:
    if re.fullmatch("https://www.books.com.tw/web/sys_saletopb/books/(\d+)/[?]loco=P_0002_(\d+)",url['href']) != None:
        print(url.text+':'+url['href'])


#re.compile()取代line8-11
for url in soup.find_all('a',href = re.compile("[?]loc=P_0002_(\d+)")):
    print(url.text+':'+url['href'])
    