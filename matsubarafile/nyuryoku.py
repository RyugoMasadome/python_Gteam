import sys
args = sys.argv

first_sent = int(args[1])
second_sent = int(args[2])
save_sent =""
animalist = ["giraffe","tiger","zebra","elephant","lion"]

save_sent = animalist[first_sent]
animalist[first_sent]  = animalist [second_sent]
animalist[second_sent] = save_sent

print(animalist)