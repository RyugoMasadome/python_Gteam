import sys
args = sys.argv

#リストの作成
animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

#引数を変数に代入
number = int(args[1])
name = args[2]

#要素の追加
animals.insert(number, name)

#リストの末尾を削除
del animals[5]

#リストを昇順にして表示
print(sorted(animals), end="")
