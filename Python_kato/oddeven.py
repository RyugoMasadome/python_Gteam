import sys
args = sys.argv

#引数で整数を入力する
number = int(args[1])

#条件分岐を作成
if number % 2 == 0:
    print("偶数です", end="")
else:
    print("奇数です", end="")