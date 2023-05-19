import sys
args = sys.argv

animalist = ["giraffe","tiger","zebra","elephant","lion"]

animal_pickup_number = int(args[1]) 
animalname_pickup_name = args[2]

animalist.insert(animal_pickup_number,animalname_pickup_name)
del animalist[len(animalist)-1]
animalist.sort()
print(animalist)