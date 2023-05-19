import sys
args = sys.argv

#引数を変数に代入
# hm_class = args[1]              #値下げ対象の種別
# price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

down_type = args[1]
down_price = int(args[2])

key_list = list(hinmoku.keys())

if down_type == "果物類":
    for i in range(len(fruits)):
        hinmoku[fruits[i]] -= down_price
if down_type == "酒類":
    for i in range(len(alcohol)):
        hinmoku[alcohol[i]] -= down_price
if down_type == "麺類":
    for i in range(len(noodles)):
        hinmoku[noodles[i]] -= down_price


for i in range(len(key_list)):
    if hinmoku[key_list[i]] < 0:
        hinmoku[key_list[i]] = 1

print(hinmoku,end="")


