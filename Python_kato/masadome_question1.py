import sys
args = sys.argv

#withを追加する関数
def append_with(sentence):
    sentence = ' with '.join(sentence)

    return sentence

#空のリスト作成
sentence = []

#単語をリストに格納するループ処理
for i in range(len(args)):
    if i == 0:
        continue
    sentence.append(args[i])

#withを追加する関数を呼び出す
sentence = append_with(sentence)

#文章を表示する
print(sentence)