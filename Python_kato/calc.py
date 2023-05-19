import sys
args = sys.argv

#引数を変数に代入
num1 = int(args[1])
num2 = int(args[2])
num3 = int(args[3])

#足し算をする
total = num1 + num2 + num3

#結果を表示
print(total, end="")