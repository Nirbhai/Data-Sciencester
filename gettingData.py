#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Learn how to scrap data from indian government websites for 
policy analysis and other information extraction,
civilian data scientist.


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
# print(first_para)
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

def paragraph_mentions(text: str,
                       keyword: str) -> bool:
    """Returns True if a <p> inside the text mentions keyword"""
    
    soup = BeautifulSoup(text, 'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]
    return any(keyword.lower() in para.lower()
               for para in paragraphs)





def congress():
    from bs4 import BeautifulSoup
    import requests
    
    ### Congress talking about lockdowns
    
    url = "https://www.house.gov/representatives"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    all_urls = [ a['href']
                for a in soup('a')
                if a.has_attr('href')]
    print( len(all_urls) )
    
    import re
    # must start with http:// or https://
    # must end with .house.gov or .house.gov/
    regex = r"^https?://.*\.house.gov/?$"
    
    # some testing for this regex
    assert re.match(regex, "http://joel.house.gov")
    assert re.match(regex, "https://joel.house.gov")
    assert re.match(regex, "http://joel.house.gov/")
    assert re.match(regex, "https://joel.house.gov/")
    assert not re.match(regex, "joel.house.gov")
    assert not re.match(regex, "joel.house.gov/")
    assert not re.match(regex, "joel.house.com")
    
    good_urls = [ url for url in all_urls if re.match(regex, url)]
    
    print( len(good_urls))
    
    good_urls = list(set(good_urls))
    print( len(good_urls))
    
    from typing import Dict, Set
    
    press_releases: Dict[str, Set[str]] = {}
    print("fetching press releases")
    for i, house_url in enumerate(good_urls):
        html = requests.get(house_url).text
        soup = BeautifulSoup(html, 'html5lib')
        pr_links = {a['href'] 
                    for a in soup('a') 
                    if 'press releases' in a.text.lower()}
        press_releases[house_url] = pr_links
        print(f"{i}. {house_url}: {pr_links}")
    print("press releases fetched")
    text = "<body><h1>Facebook</h1><p>Twitter</p>"
    assert not paragraph_mentions(text, "Facebook")
    assert paragraph_mentions(text, "Twitter")
    
    for house_url, pr_links in press_releases.items(): 
        for pr_link in pr_links:
            url = f"{house_url}/{pr_link}"
            text = requests.get(url).text
            if paragraph_mentions(text, 'data'): 
                print(f"{house_url}")
                break # done with this house_url

def github_api_access():
    import requests, json 
    github_user = "Nirbhai"
    endpoint = f"https://api.github.com/users/{github_user}/repos"
    repos = json.loads(requests.get(endpoint).text)
    from collections import Counter 
    from dateutil.parser import parse
    dates = [parse(repo["created_at"]) for repo in repos]
    month_counts = Counter(date.month for date in dates) 
    weekday_counts = Counter(date.weekday() for date in dates)
    print(month_counts, weekday_counts)

def main():
    CONSUMER_KEY = "XsgVCpQcUGXkCRJggee7WBWZ1"
    CONSUMER_SECRET = "48ejl7yQUG7Qp6XO0mPWNa0elqEZyV3k1qdEZxdlSRbpBtBMba"
    
    import webbrowser
    from twython import Twython
    
    # temporary client to retrieve an authentication URL
    temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
    temp_creds = temp_client.get_authentication_tokens()
    url = temp_creds['auth_url']
    
    # Now visit that URL to authorize the application and get a PIN
    print(f"go visit {url} and get the PIN code and paste it below") 
    webbrowser.open(url)
    PIN_CODE = input("please enter the PIN code: ")
    
    # Now we use that PIN_CODE to get the actual tokens
    auth_client = Twython(CONSUMER_KEY,
                          CONSUMER_SECRET,
                          temp_creds['oauth_token'],
                          temp_creds['oauth_token_secret'])
    final_step = auth_client.get_authorized_tokens(PIN_CODE)
    ACCESS_TOKEN = final_step['oauth_token']
    ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']
    
    # And get a new Twython instance using them.
    twitter = Twython(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET)
    
    # Search for tweets containing the phrase "data science"
    for status in twitter.search(q='"data science"')["statuses"]: user = status["user"]["screen_name"]
    text = status["text"]
    print(f"{user}: {text}\n")
    
    from twython import TwythonStreamer
    
    # Appending data to a global variable is pretty poor form
    # but it makes the example much simpler
    tweets = []
    
    class MyStreamer(TwythonStreamer):
        def on_success(self, data):
            """
            What do we do when twitter sends us data?
            Here data will be a Python dict representing a tweet
            """
            # We only want to collect English-language tweets
            if data.get('lang') == 'en':
                tweets.append(data)
                print(f"received tweet #{len(tweets)}")
    
            # Stop when we've collected enough
            if len(tweets) >= 100:
                self.disconnect()
    
        def on_error(self, status_code, data):
            print(status_code, data)
            self.disconnect()
    
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # starts consuming public statuses that contain the keyword 'data'
    stream.statuses.filter(track='data')
    
    # if instead we wanted to start consuming a sample of *all* public statuses
    # stream.statuses.sample()
    
    from collections import Counter
    top_hashtags = Counter(hashtag['text'].lower() 
                           for tweet in tweets
                           for hashtag in tweet["entities"]["hashtags"])
    print(top_hashtags.most_common(5))


































if __name__ == "__main__": main()