"""
pandas.DataFrame, SeriesとPython標準のリストを相互に変換
https://note.nkmk.me/python-pandas-list/
pandas.DataFrameとSeriesを相互に変換
https://note.nkmk.me/python-pandas-dataframe-series-conversion/



"""
"""
import pandas as pd
import csv

all_list = pd.read_csv("/Users/inubushihikari/Desktop/Python/mr.children/csv/sample.csv")
print(all_list)
"""
search = input("好きな文字を入力:")
print("あなたが調べたいのは" + search)

import csv
csv_file = open("./csv/sample.csv", "r",  errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#先生、行ごと消しました(｀･ω･´)ゞ

for row in f:
    #print(row)

    if search in row:
        print(row[5])
    #else:
        #print("No Hit!!")

"""
mylist = ["aaa","bbb","ccc"]
if search in mylist:
    print(search)
else:
    print("No Hit-dayo!!")
"""



mylist = ["aaa","bbb","ccc"]
