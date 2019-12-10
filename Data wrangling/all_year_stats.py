# %%
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
import time


# %%

url = "https://www.espn.com/college-football/stats/team/_/season/2018"
sourcecode = requests.get(url)
planetext = sourcecode.text
code = BeautifulSoup(planetext, "html.parser")

# %%

data = code.find_all("tr", class_="Table__TR Table__TR--sm Table__even")


# %%

header = code.find_all("th", class_="Table__TH")

# %%

teamname = code.find_all("tr", class_="Table__TR Table__TR--sm Table__even")


for x in teamname:
    print(x)

# TODO find a way to get team names
# %%

df = pd.DataFrame()
for x in header:
    try:
        test = x.contents[0]
        col = str(test).split("=")[2].split('"')[1]
        df[col] = 0
        print(col)
    except:
        print("Column not found")


df = df.drop([''], axis=1)
# %%
# dataindex = x.attrs.get('data-idx')
# listofdata = list(x)
# single = listofdata(x)[1]
# coldata = str(single).split(">")[2]
# inputdata = re.sub("[^0-9]", "", coldata)
# df.loc[dataindex, "Total Yards"] = inputdata

start = time.time()
for x in data:
    try:
        dataindex = x.attrs.get('data-idx')
        listofdata = list(x)
        single = listofdata[0]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9,.]", "", coldata)
        df.loc[dataindex, "Games Played"] = inputdata

        single = listofdata[1]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9,.]", "", coldata)
        df.loc[dataindex, "Total Yards"] = inputdata

        single = listofdata[2]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9,.]", "", coldata)
        df.loc[dataindex, "Yards Per Game"] = inputdata

        single = listofdata[3]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9,.]", "", coldata)
        df.loc[dataindex, "Passing Yards"] = inputdata

        single = listofdata[4]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9,.]", "", coldata)
        df.loc[dataindex, "Passing Yards Per Game"] = inputdata

        single = listofdata[5]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9,.]", "", coldata)
        df.loc[dataindex, "Rushing Yards"] = inputdata

        single = listofdata[6]
        coldata = str(single).split(">")[2]
        inputdata = float(re.sub("[^0-9,.]", "", coldata))
        df.loc[dataindex, "Rushing Yards Per Game"] = inputdata

        single = listofdata[7]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9.,]", "", coldata)
        df.loc[dataindex, "Total Points"] = inputdata

        single = listofdata[8]
        coldata = str(single).split(">")[2]
        inputdata = re.sub("[^0-9.,]", "", coldata)
        df.loc[dataindex, "Total Points Per Game"] = inputdata

        print(f"Finished {dataindex}")
    except:
        print(f"{dataindex} did not wotk")


print(start - time.time())


# %%


teamnames = code.find_all('a')
teamlist = []
for x in teamnames:
    try:
        if len(x.get("alt")) > 0:
            teamlist.append(x)
    except:
        pass

# %


# %%

index = code.find_all('a')
listofhrefs = []
for x in index:
    try:
        if "id" in x.get("href"):
            listofhrefs.append(x.get("href"))
    except:
        continue

# %%
listofteams = []
count = 0
for x in listofhrefs:
    try:
        name = x.split("/")[6]
        if name not in listofteams:
            listofteams.append(name)
    except IndexError:
        print(f"{x} does not contain a team")

listofteams.remove("id")

# %%
jointeams = {}
counter = -1
for x in listofteams:
    print(x)
    counter += 1
    jointeams[counter] = x

jointeams = pd.DataFrame.from_dict(jointeams, orient='index')


# %%

df = df.reset_index()
jointeams = jointeams.reset_index()
df["index"] = df["index"].astype(int)
jointeams["index"] = jointeams["index"].astype(int)
teamstats = df.merge(jointeams, left_on="index", right_on="index", how="left")
teamstats = teamstats.drop(["index"], axis=1)


# %%

# make team directory in python. make teamstat file than make loop to do all files in schedule
