from decimal import Decimal, ROUND_HALF_UP

def calcsalary(salary):
    border = 1000000
    payment, tax = 0, 0
    if salary >= border:
        tax = 0.2*(salary-border)+100000
    else:
        tax = 0.1*salary

    # 小数点以下で四捨五入
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    payment = salary-tax
    return payment, tax
