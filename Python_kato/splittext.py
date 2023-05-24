import sys
args = sys.argv

#引数を代入
sentence = args[1]
number = int(args[2])

#文字列を分割
sentence = sentence.split()

#結果を表示
print(sentence[number-1], end="")