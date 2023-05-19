import sys
args = sys.argv

m_scr = int(args[1])
l_scr = int(args[2])
e_scr = int(args[3])

sum_scr = m_scr + l_scr + e_scr

if ((e_scr>=70)and(l_scr>=70)and(m_scr>=70)):
    print("合格")
else:
    if(sum_scr>=220):

        if(e_scr>=50)and(l_scr>=50)and(m_scr>=50):
            print("合格")
        else:
            print("不合格")
    else:
        print("不合格")

