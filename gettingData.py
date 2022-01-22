#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""




Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


*********************************

Run below commands to verify you are in correct environment and branch:
    !conda info -e
    !git branch -a

*********************************


"""

def get_domain(email_address: str) -> str:
    """split on "@" and return the last piece"""
    return email_address.lower().split("@")[-1]

assert get_domain("nirbhai@zencat.studio") == "zencat.studio"
assert get_domain("1jobplz@zencat.studio") == "zencat.studio"

from os import path



with open(path.expanduser("~/Documents/Data-Sciencester/Data/tab_delimited_stock_prices.txt"), "w") as f:
    f.write("""6/20/2014\tAAPL\t90.91
6/20/2014\tMSFT\t41.68
6/20/2014\tFB\t64.5
6/19/2014\tAAPL\t91.86
6/19/2014\tMSFT\t41.51
6/19/2014\tFB\t64.34
""")

import csv

def process(date: str, symbol: str, closing_price: float) -> None:
    # dummy function
    assert closing_price > 0.0

with open(path.expanduser("~/Documents/Data-Sciencester/Data/tab_delimited_stock_prices.txt"), "r") as f:
    tab_reader = csv.reader(f, delimiter='\t')
    for row in tab_reader:
        date            = row[0]
        symbol          = row[1]
        closing_price   = float(row[2])
        process(date, symbol, closing_price)



with open(path.expanduser("~/Documents/Data-Sciencester/Data/colon_delimited_stock_prices.txt"), 'w') as f:
    f.write("""date:symbol:closing_price
6/20/2014:AAPL:90.91
6/20/2014:MSFT:41.68
6/20/2014:FB:64.5
""")

with open(path.expanduser("~/Documents/Data-Sciencester/Data/colon_delimited_stock_prices.txt"), 'r') as f:
    colon_reader = csv.DictReader(f, delimiter=':')
    for dict_row in colon_reader:
        date            = dict_row["date"]
        symbol          = dict_row["symbol"]
        closing_price   = float(dict_row["closing_price"])
        process(date, symbol, closing_price)

# Even if your file doesn’t have headers, 
# you can still use DictReader by passing it the keys as a fieldnames parameter

todays_prices = { "AAPL": 90.91,
                 "MSFT": 41.68,
                 "FB": 64.5
                 }

with open(path.expanduser("~/Documents/Data-Sciencester/Data/comma_delimited_stock_prices1.txt"), 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for stock, price in todays_prices.items():
        csv_writer.writerow([stock, price])

# use csv.writer to write csv files
# don't use simple "f.write" to write csv files - (like I did above, twice)
# it will inadvertently lead to errors one day

import requests
from bs4 import BeautifulSoup

# Joel Grus, the CEO of Data Sciencester put a dummy HTML file on GitHub.
# Recall that whitespace-separated strings get concatenated.

url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")

html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')


first_para = soup.find('p')
print(first_para)
# returns <p id="p1">This is the first paragraph.</p>
# full p tag with all its contents

first_para_text = first_para.text
assert soup.p.text == first_para_text

first_para_words = first_para_text.split()

# extract a tag’s attributes by treating it like a dict
first_para_id  = soup.p['id']            # raises KeyError if no 'id'
first_para_id2 = soup.p.get('id')        # returns None if no 'id'

# to get mutiple tags at once
all_paras = soup.find_all('p')
assert all_paras == soup('p')

paras_with_ids = [ p for p in soup('p') if p.get('id') ]

# to find tags with a specific class
imp_paras1 = soup( 'p', {'class': 'important'} )
imp_paras2 = soup('p', 'important')
imp_paras3 = [ p for p in soup('p')
              if 'important' in p.get('class', [])
              ]

assert imp_paras1 == imp_paras2 and imp_paras2 == imp_paras3
#print(imp_paras1, imp_paras2, imp_paras3)

# to find every <span> element that is contained inside a <div> element

# Warning: will return the same <span> multiple times 
# if it sits inside multiple <div>s.
# Be more clever if that's the case. 
spans_inside_divs = [span
                     for div in soup('div')   # for each <div> on the page
                     for span in div('span')] # find each <span> inside it




### Congress talking about lockdowns

url = "https://www.house.gov/representatives"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

all_urls = [ a['href']
            for a in soup('a')
            if a.has_attr('href')]
print( len(all_urls) )



































