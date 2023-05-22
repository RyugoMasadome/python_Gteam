import sys

args = sys.argv

# 配列内の1番目の要素以降を数値型にして取り出し、resに加える処理
res = sum([int(num) for num in args[1:]])

print(res, end="")