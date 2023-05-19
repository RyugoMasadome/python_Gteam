import sys
args = sys.argv

# 半角空白で分けたリストをwordsに格納する
words = args[1].split(' ')
index = int(args[2])

print(words[index-1], end="")
