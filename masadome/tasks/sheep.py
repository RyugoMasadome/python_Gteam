import sys

args = sys.argv
times = int(args[1])

assert times >= 1

for i in range(1, times+1):
    print(f'ひつじが{i}匹')
    