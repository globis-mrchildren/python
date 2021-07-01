search1 = input("アルバム名:")


print("あなたが調べたいのは" + search1 + search2)

import pandas as pd
from pandas.io.parsers import count_empty_vals

all_list = pd.read_csv("./csv/sample.csv")

for index, row in all_list.iterrows():
    if search1 in row[5] and search2 in row[5]:
        print(row[1],search1 + "の数は" + str(row[5].count(search1)),search2 + "の数は" + str(row[5].count(search2)))

