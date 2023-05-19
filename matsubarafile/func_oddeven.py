import sys
args = sys.argv

in_stats = []
get_stats = []
in_value = 1

def calcvalue(value):
    if value%2 == 0:
        print(str(value) + "は偶数")
    else:
        print(str(value) + "は奇数")

while(in_value != len(args)):
    get_stats.append(int(args[in_value]))
    calcvalue(get_stats[in_value-1])

    in_value = in_value +1 
