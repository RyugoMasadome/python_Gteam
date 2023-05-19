import sys
args = sys.argv

#引数で整数を入力する
score_mat = int(args[1])
score_jap = int(args[2])
score_eng = int(args[3])

if score_mat >= 50 and score_jap>= 50 and score_eng >= 50: 
    if (score_mat >= 70 and score_jap >= 70 and score_eng >= 70) or ((score_mat + score_jap + score_eng) >= 220):
        print("合格", end="")
    else:
        print("不合格", end="")
else:
    print("不合格", end="")