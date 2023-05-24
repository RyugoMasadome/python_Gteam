import sys
args = sys.argv
from datetime import date

#大人の料金計算
def calc_fee_adult(day, number):
    #休日料金のとき
    if (day == 0) or (day == 6):
        fee = 2400 * number
    #平日のとき
    else:
        fee = 2000 * number
   
    #料金を返す
    return fee

#子供の料金計算
def calc_fee_child(day, number):
    #休日料金のとき
    if (day == 0) or (day == 6):
        fee = 1500 * number
    #平日のとき
    else:
        fee = 1200 * number
   
    #料金を返す
    return fee

#日付を取得し曜日を表す数字に変換
day = args[1]
day = [day[:4], day[5:6], day[6:]]
day = date(int(day[0]), int(day[1]), int(day[2]))
day = day.strftime("%w")

#大人と子供それぞれの料金を計算
fee_adult = calc_fee_adult(int(day), int(args[2]))
fee_child = calc_fee_child(int(day), int(args[3]))

#合計料金を計算
fee = fee_adult + fee_child

#合計料金を表示
print(fee, end="")