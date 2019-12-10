# %%

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


 # %%


df = pd.read_csv("Data wrangling/data/2018_schedule.csv")

# %%
df = df.dropna(subset=["Team 2"])
df = df.drop(df.tail(1).index,)
# %%


df["Date"] = pd.to_datetime(df["Date"])
week1 = df.loc[0, "Date"]
# week1 -= timedelta(7)

weekdf = pd.DataFrame()
numweeks = range(0, 24)

for x in numweeks:
    week1_new = (x * 7)
    weekstart = week1 + timedelta(week1_new)
    daysbetween = 7-1
    weekend = weekstart + timedelta(daysbetween)
    weekdf = weekdf.append(
        {"End": weekend, "Start": weekstart,  "week": f"{x +1}"}, ignore_index=True)

    print(f"week {x +1}, is from {weekstart} to {weekend}")

df["Home"] = 0
df["Away"] = 0

# %%

for x in df.index:
    if "at" in df.loc[x, "Team 1"]:
        home = df.loc[x, "Team 1"]
        away = df.loc[x, "Team 2"]
        df.loc[x, "Home"] = home
        df.loc[x, "Away"] = away

    if "at" in df.loc[x, "Team 2"]:
        home = df.loc[x, "Team 2"]
        away = df.loc[x, "Team 1"]
        df.loc[x, "Home"] = home
        df.loc[x, "Away"] = away


# %%
for x in df.index:
    print(f'Working on {x} of {len(df)}')
    mew = df[df.index == x]
    for t in df["Date"]:
        for y in numweeks:
            if weekdf.loc[y, "Start"] >= t <= weekdf.loc[y, "End"]:
                week = weekdf.loc[y, "week"]
                df.loc[x, "Week"] = week
                continue
            else:
                continue

# %%

dflen = len(df)
dflen += 1
dflength = range(0, dflen)

t = df.loc[0, "Date"]
# %%
for y in numweeks:
    if weekdf.loc[y, "Start"] <= t >= weekdf.loc[y, "End"]:
        print(f"{weekdf.loc[y, 'Start']}, \n{t} \n{weekdf.loc[y, 'End']}")
        print("true")
    else:
        print("false")
        print(f"{weekdf.loc[y, 'Start']}, \n{t} \n{weekdf.loc[y, 'End']}")
        # week = weekdf.loc[y, "week"]
        # df.loc[x, "Week"] = week

# TODO find home and away teams with for loop for each row dflength
# %%
# %%

# %%
