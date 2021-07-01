search = input("好きな言葉は？")
print(search + "の出現回数は…")

import pandas as pd
from pandas.io.parsers import count_empty_vals

all_list = pd.read_csv("./csv/sample.csv")

count = 0

for index, row in all_list.iterrows():
    count = count + row[5].count(search)

print("全部で" + str(count) + "個")

"""
search = input("好きな単語を入力:")
print("あなたが調べたいのは" + search)

import pandas as pd
from pandas.io.parsers import count_empty_vals

all_list = pd.read_csv("./csv/sample.csv")

for index, row in all_list.iterrows():
    if search in row[5]:
        print(row[1],row[5].count(search))
"""

