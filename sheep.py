import sys
args = sys.argv

times = int(args[1])
k=1
for i in range(times):
    desc = "ひつじが{0}匹".format(k)
    print(desc)
    k=k+1