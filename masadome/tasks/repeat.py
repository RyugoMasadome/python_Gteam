import sys

args = sys.argv

now = 0

assert int(args[1]) > 0, '制約外の値が含まれています'


print('Just 100!' if 100 % int(args[1]) == 0 else 'Over!', end='')
