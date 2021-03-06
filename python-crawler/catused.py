# -*- coding: utf-8 -*-
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
"""
@author: cbchien
"""

results = []
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=5&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1007_36_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1007_36_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1013_63_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
"http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=5&epp=90&sf=relevance&so=false"]

for url in urls:
    a = requests.get(url)
    maxnum = len(results)
    
    soup = BeautifulSoup(a.text, 'html.parser')
    
    allitem = soup.find_all("span", {"itemprop":"name"}, True)
    for name in allitem:
        results.append({
                    "name": name['content']
                    })
    print("Total of ",  len(allitem))
    print("start ", maxnum)
    print("End ", (maxnum + len(allitem)))
    c = soup.find_all("span", {"itemprop":"category"}, True)
    u = soup.find_all("span", {"itemprop":"url"}, True)
    p = soup.find_all("li", {"class" : "final"}, True)
    h = soup.find_all("p", {"class" : "hours"}, True)
    y = soup.find_all("p", {"class" : "year"}, True)
    l = soup.find_all("p", {"class" : "Location"}, True)
    for item in range(maxnum, (maxnum + len(allitem))):
        print(item)
        print((item-maxnum))
        results[item]["category"] = c[item-maxnum].text
        results[item]["url"] = u[item-maxnum]['content']
        results[item]["price"] = re.sub('[\s+]', '', p[item-maxnum].text)
        results[item]["hour"] = re.sub('[\s+]', '', h[item-maxnum].text)
        results[item]["year"] = re.sub('[\s+]', '', y[item-maxnum].text)
        results[item]["location"] = re.sub('[\s+]', '', l[item-maxnum].text)

df = pd.DataFrame(results)

df.to_csv("catused.csv", sep=',', encoding='utf-8')
    
'''
Track Excavators
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=5&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=6&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1005_152551_&et=_1005_77_&mfc=100&srg=_1_SWUS_&pnr=7&epp=90&sf=relevance&so=false"]

Backhoe Loaders
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1003_9_&mfc=100&srg=_1_SWUS_&pnr=5&epp=90&sf=relevance&so=false"]

Forklifts
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1023_91_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false"]

Motor Graders
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1007_36_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1007_36_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false"]

Track Loaders
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1013_63_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false"]

Track Type Tractors
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1014_66_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false"]

Skid Steel Loaders
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1011_38_&et=_1011_55_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false"]

Wheel Loader
urls = ["http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=1&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=2&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=3&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=4&epp=90&sf=relevance&so=false",
        "http://catused.cat.com/en/search_results_wide.html?et=_1016_152504_&et=_1016_79_&mfc=100&srg=_1_SWUS_&pnr=5&epp=90&sf=relevance&so=false"]

'''


