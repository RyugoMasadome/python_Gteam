for i in range(1,21):
    if(i % 15 == 0):
        print("fizz Buzz")
        continue
    if(i % 3 == 0):
        print("fizz")
        continue
    if(i % 5 ==0):
        print("Buzz")
    print(i)