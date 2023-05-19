import sys

args = sys.argv

rank = int(args[1])

assert 1 <= rank <= 10
populationRank = (
    'China', 
    'India', 
    'U.S.A', 
    'Indonesia', 
    'Pakistan', 
    'Brazil', 
    'Nigeria', 
    'Bangladesh', 
    'Russia', 
    'Mexico'
    )

print(f'{populationRank[rank-1]}', end='')

