import sys

args = sys.argv
num = int(args[1])

print('奇数' if num % 2 == 1 else '偶数')