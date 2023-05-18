import sys
args = sys.argv

number = int(args[1])
sum = 0
rupe_checker = 0 
while(sum <=100):
    sum = sum + number
    if number == 0 :
        rupe_checker = 1
        break
    elif sum == 100 :
        print("Just 100!" ,end ="")
        break
    elif sum > 100:
        print("Over!" ,end ="")

if(rupe_checker == 1):
    print("ERROR" ,end ="")