# %%
from bs4 import BeautifulSoup
import pandas
import numpy
import requests


# %%

years = range(2010, 2020)
for x in years:
    Url = f"https://www.masseyratings.com/scores.php?s=cf{x}&sub=ncaa-d1&all=1&sch=on"
    url_sourcecode = requests.get(Url)
    urlPlaneText = url_sourcecode.text
    urlSoup = BeautifulSoup(urlPlaneText, "html.parser")
    pre = urlSoup.find_all("pre")[0]
    stringpre = pre.string
    test = open(
        f"Data wrangling/data/{x}_schedule.txt", "a+")
    test.write(stringpre)
    test.close()


# %%
