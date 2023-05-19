import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

#リストの作成
station_distance = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

#引数を変数に代入
station_1 = args[1]
station_2 = args[2]

#要素の追加
distance = station_distance[station_1] - station_distance[station_2]
if distance < 0:
    distance = distance * (-1)

distance = round(distance, 2)

print(distance, end="")
