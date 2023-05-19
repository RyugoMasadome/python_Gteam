import sys
args = sys.argv

sta_list = {'東京':0.00, '品川':6.78, '新横浜':25.54, '名古屋':342.02, '京都':476.31, '新大阪':515.35}

sta_sta = sta_list[args[1]]
sta_fin = sta_list[args[2]]

dis = format(abs(float(sta_sta) - float(sta_fin)), '.2f')

print(dis,end="")
