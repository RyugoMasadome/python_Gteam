import sys

args = sys.argv

now = 0

while now != 100:
    now = now + int(args[1])
    if now > 100:
        print('Over!', end="")
        break

if now == 100: print('Just 100!', end="")