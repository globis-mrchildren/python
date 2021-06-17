search = input("好きな文字を入力:")
print("あなたが調べたいのは" + search)

import pandas as pd
import csv

all_list = pd.read_csv("./csv/sample.csv")

"""
import csv
csv_file = open("./csv/sample.csv", "r",  errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
"""

for row in f:
    if search in row:
        print(row[5])
    #else:
        #print("No Hit!!")


