import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv

departure = args[1]

arrival = args[2]

distances = {
    '東京':0.00,
    '品川':6.78,
    '新横浜':25.54,
    '名古屋':342.02,
    '京都':476.31,
    '新大阪':515.35
}


try:
    # 絶対値の取得
    dist = abs(distances[arrival]-distances[departure])

    # 小数第3位で四捨五入
    dist = Decimal(str(dist)).quantize(Decimal("0.00"), ROUND_HALF_UP)

    print(dist, end="")

except:
    print('のぞみの停車駅を引数に設定してください', end="")