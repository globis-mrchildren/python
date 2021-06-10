import csv

csv_file = open("./csv/sample.csv", "r", encoding="", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    print(row)

string = input("文字列を入力してください:")
print("文字列", string, "が入力されました。")

mylist = ['aaa','bbb','ccc'] 

if string in mylist:
    print('含まれていました')
else:
    print('含まれておりませんでした')