import sys
args = sys.argv

#リストの作成
countries = ("China", "India", "U.S.A", "Indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

#引数を変数に代入
rank = int(args[1])

#リストを昇順にして表示
print(countries[rank], end="")

