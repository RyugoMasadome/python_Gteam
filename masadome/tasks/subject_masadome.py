import sys

args = sys.argv

math, japanese, english = [int(num) for num in args[1:]]

passed1, passed2 = False, False
if (math >= 70 and japanese >= 70 and english >= 70) or sum([math, japanese, english]) >= 220:
    passed1 = True

if math >= 50 and japanese >= 50 and english >= 50:
    passed2 = True

print("合格" if passed1 and passed2 else "不合格", end="")

