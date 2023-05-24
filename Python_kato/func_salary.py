from decimal import Decimal, ROUND_HALF_UP

#支給額と税額を計算する関数を作成
def calcsalary(salary):
    salary = float(salary)
    if salary <= 1000000:
        tax = Decimal(str(salary * 0.1)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        payment = int(salary) - tax
    else:
        tax = Decimal(str(1000000 * 0.1 + (salary - 1000000) * 0.2)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        payment = int(salary) - tax

    return payment, tax