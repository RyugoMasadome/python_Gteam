import sys
from decimal import Decimal,ROUND_HALF_UP
args = sys.argv

startpoint = args[1]
endpoint = args[2]

station_name  =["東京","品川","新横浜","名古屋","京都","新大阪"]
stations_distance = [ 0.00 , 6.78 , 25.54 , 342.02 , 476.31 , 515.35]



def station_position(sta):
    pointer_sta_n =0
    check =0
    while(check ==0):
        if(sta == station_name[pointer_sta_n]):
            check =1
            return pointer_sta_n
            break
        else:
            pointer_sta_n = pointer_sta_n +1

def sta_dist (start,end):
    dist = stations_distance[end] - stations_distance[start]
    if(dist < 0):
        dist = dist * (-1)
    dist = Decimal(str(dist)).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
    return dist

print(sta_dist(station_position(startpoint),station_position(endpoint)) ,end="") 
    