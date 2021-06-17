search = input("好きな文字を入力:")
print("あなたが調べたいのは" + search)

import pandas as pd

all_list = pd.read_csv("./csv/sample.csv")

for index, row in all_list.iterrows():
    if search in row[1]:
        print(row[5])
        break
    #else:
        #print("No Hit!!")
