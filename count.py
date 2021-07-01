search = input("好きな言葉は？")
print(search + "の出現回数は…")

import pandas as pd
from pandas.io.parsers import count_empty_vals

all_list = pd.read_csv("./csv/sample.csv")

count = 0

for index, row in all_list.iterrows():
    count = count + row[5].count(search)

print("全部で" + str(count) + "個")