import sys
args = sys.argv

#引数を変数に代入
hm_class = args[1]              #値下げ対象の種別
price_down = int(args[2])   #値下げ額

#品目（品名と価格）を辞書型で定義
hinmoku = {"リンゴ":80 , "みかん":198, "バナナ":150, "ビール":360, "日本酒":580, "ラーメン":380, "うどん":128, "パスタ":258}

#区分ごとの定義
fruits = ("リンゴ", "みかん", "バナナ")            #果物類をタプルで定義
alcohol = ("ビール", "日本酒")                         #酒類をタプルで定義
noodles = ("ラーメン", "うどん", "パスタ")   #麺類をタプルで定義

#ここ以降にプログラムを書く
#果物類のとき
if hm_class == "果物類":
    for name_h in hinmoku.keys():
        for i in range(len(fruits)):
            if (name_h == fruits[i]) and (hinmoku[name_h] - price_down > 0):
                hinmoku[name_h] -= price_down
            elif name_h == fruits[i]:
                hinmoku[name_h] = 1
#酒類名のとき
elif hm_class == "酒類":
    for name_h in hinmoku.keys():
        for i in range(len(alcohol)):
            if (name_h == alcohol[i]) and (hinmoku[name_h] - price_down > 0):
                hinmoku[name_h] -= price_down
            elif name_h == alcohol[i]:
                hinmoku[name_h] = 1

#上記以外のとき
else:
    for name_h in hinmoku.keys():
        for i in range(len(noodles)):
            if (name_h == noodles[i]) and (hinmoku[name_h] - price_down > 0):
                hinmoku[name_h] -= price_down
            elif name_h == noodles[i]:
                hinmoku[name_h] = 1

print(hinmoku, end="")