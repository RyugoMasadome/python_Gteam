import sys
args = sys.argv
from decimal import Decimal, ROUND_HALF_UP

#引数で整数を入力する
salary = float(args[1])

if salary <= 1000000:
    tax = Decimal(str(salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    payment = int(salary) - tax
else:
    tax = Decimal(str(1000000 * 0.1 + (salary - 1000000) * 0.2)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    payment = int(salary) - tax

print("支給額:" + str(payment) + "、税額:" + str(tax), end="")
