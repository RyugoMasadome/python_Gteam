import sys
args = sys.argv

num = int(args[1])
sum = 0

while True:
    sum = sum + num
    if(sum ==100):
        print("Just 100!")
        break
    elif(sum>100):
        print("Over!")
        break
    elif(sum==0):
        print("error")
        break