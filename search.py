search1 = input("好きな単語1:")
search2 = input("好きな単語2:")

print("あなたが調べたいのは" + search1 + search2)

import pandas as pd
from pandas.io.parsers import count_empty_vals

all_list = pd.read_csv("./csv/sample.csv")

count1 = 0
count2 = 0

for index, row in all_list.iterrows():
    if search1 in row[5] or search2 in row[5]:
        count1 = count1 + row[5].count(search1)
        count2 = count2 + row[5].count(search2)
        print(row[1],search1 + "の数は" + str(row[5].count(search1)),search2 + "の数は" + str(row[5].count(search2)))

print(search1 + "の数は" + str(count1),search2 + "の数は" + str(count2))

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

