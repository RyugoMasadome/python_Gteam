import sys

# 品物名と値段の定義
goods = {
    "リンゴ":80, "みかん":198, "バナナ":150,
    "ビール":360, "日本酒":580, 
    "ラーメン":380, "うどん": 128, "パスタ":258
}

# どのジャンルにどの品物が属しているか
fruits = ('リンゴ', 'みかん', 'バナナ')
alcohol = ('ビール', '日本酒')
noodles = ('ラーメン', 'うどん', 'パスタ')

# ジャンル名をキーに、タプルを値に持つ辞書genreの定義
genre = {'果物類':fruits, '酒類':alcohol, '麺類':noodles}

# いつもの
args = sys.argv

# 選択されたジャンルと値引き価格設定
picked_genre = args[1]
discount = int(args[2])

# 選択されたジャンルのタプルを取り出す
selected_genre = genre[picked_genre]

# 品物のキー一覧を取得し
for k in list(goods.keys()):
    # もしタプルの中に品物のキーがあったら
    if k in selected_genre:
        # 品物の値段を変更する
        goods[k] = max(1, goods[k]-discount)

print(goods, end="")

