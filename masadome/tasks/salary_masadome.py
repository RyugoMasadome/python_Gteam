import sys
from decimal import Decimal, ROUND_HALF_UP

args = sys.argv

salary = int(args[1])

# 100万がボーダー
border = 1000000
tax = 0

if salary > border:
    tax = (salary-border)*0.2 + 100000
else:
    tax = salary*0.1

# Decimalモジュールによる四捨五入
# 税額の四捨五入
tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)

# 給与は支給額-税額
payment = salary-tax
print(f'支給額:{payment}、税額:{tax}', end="")
