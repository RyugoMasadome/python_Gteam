import sys
args = sys.argv

sheep_value = int(args[1])
count_sheep = 0

while (count_sheep != sheep_value):
    count_sheep = count_sheep +1
    if(count_sheep == sheep_value):
        print("ひつじが" + str(count_sheep) + "匹")
        break
    else:
        print("ひつじが" + str(count_sheep) + "匹")
        continue