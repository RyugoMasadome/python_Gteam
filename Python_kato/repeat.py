import sys
args = sys.argv

#引数で整数を入力する
number = int(args[1])

#足し算の初期値を代入
count = 0

#ループ処理
while count < 100:
    #足し算を行う
    count += number
    if count == 100:
        print("Just 100!", end="")
    elif count >= 100:
        print("Over!", end="")
