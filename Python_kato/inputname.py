import sys
args = sys.argv

#ユーザーから直接入力
user = input("What's your name?")

#引数を変数に代入
name = args[1]

#結果を表示
print("Hello " + name, end="")