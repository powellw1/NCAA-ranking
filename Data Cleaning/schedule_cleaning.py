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
week1 -= timedelta(7)

weekdf = pd.DataFrame()


for x in numweeks:
    week1_new = (x * 7)
    weekstart = week1 + timedelta(week1_new)
    daysbetween = 7-1
    weekend = weekstart + timedelta(daysbetween)
    weekdf = weekdf.append(
        {"End": weekend, "Start": weekstart,  "week": f"week {x}"}, ignore_index=True)

    print(f"week{x}, is from {weekstart} to {weekend}")


22  # %%


df["Season"] = "18-19"
df[df["Date"] ==]
# %%
df = pd.DatetimeIndex(df["Date"]).year
df = pd.to_datetime(df["Date"])

week1 = df.loc[0, "Date"]
week2 = "8/25/18"
week2 = datetime.strptime(week2, "%m/%d/%yy")

# %%

# %%

# %%

# %%
