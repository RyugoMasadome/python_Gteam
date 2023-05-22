import sys
args = sys.argv

#関数を定義
def calcvalue(num):
    #あまりを算出
    mod = num % 2

    #あまりの値から奇数偶数判定
    if mod != 0:
        print(str(num) + "は奇数")
    else:
        print(str(num) + "は偶数")


#main
for i in range(len(args)-1):
    #コマンドライン引数の数分実行
    num = int(args[i+1])
    calcvalue(num)