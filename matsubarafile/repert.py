import sys
args = sys.argv

number = int(args[1])
sum = 0
rupe_checker = 0 
while(sum <100):
    if number == 0 :
        rupe_checker = 1
        break
    elif sum == 100 :
        print("Just 100!")
    elif sum > 100:
        print("Over!")      
    else:
        sum = sum + number

if(rupe_checker == 1):
    print("ERROR")