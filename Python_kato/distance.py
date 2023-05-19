import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

#辞書の作成
station_distance = {'東京': 0.00, '品川': 6.78, '新横浜': 25.54, '名古屋': 342.02, '京都': 476.31, '新大阪': 515.35}

#引数を変数に代入
station_1 = args[1]
station_2 = args[2]

#距離を計算
distance = station_distance[station_1] - station_distance[station_2]

#絶対値にする
if distance < 0:
    distance = distance * (-1)

#小数点第二位以下を丸める
distance = round(distance, 2)

#結果の表示
print(distance, end="")
