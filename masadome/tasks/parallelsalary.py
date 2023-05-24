import sys
from func_salary import calcsalary


def toStrSalary(salary, payment, tax):
    return f'給与:{salary}、支給額:{payment}、税額:{tax}'

args = sys.argv

lst = list(map(int, args[1:]))

for salary in lst:
    payment, tax = calcsalary(salary)
    print(toStrSalary(salary, payment, tax))
