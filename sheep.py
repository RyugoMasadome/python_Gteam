import sys
args = sys.argv

#引数で整数を入力する
number = int(args[1])

#ループ処理
for i in range(1,number+1):
    print("ひつじが" + str(i) + "匹")