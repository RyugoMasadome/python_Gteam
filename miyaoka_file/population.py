import sys
args = sys.argv
rank = int(args[1]) - 1

con_tuple = ("China", "India", "U.S.A", "indonesia", "Pakistan", "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico")

print(con_tuple[rank])
