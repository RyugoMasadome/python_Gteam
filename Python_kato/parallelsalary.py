import sys
args = sys.argv
import func_salary
from decimal import Decimal, ROUND_HALF_UP

#引数で整数を入力する
for i in range(len(args)):
    if i == 0:
        continue

    salary = float(args[i])
    payment_tax = func_salary.calcsalary(args[i])
    print("給与: ", args[i], "、支給額:", payment_tax[0], "、税額: ", payment_tax[1])