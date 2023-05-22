import sys

args = sys.argv

num = args[1]
num = int(num)

primes = [1]*10**6

primes[1] = 0
divisors = []

for i in range(2, 10**6):
    if primes[i] == 0:
        continue
    divisors.append(i)
    for j in range(i*2, 10**6, i):
        primes[j] = 0

ans = []
for prime in divisors:
    while num % prime == 0 and num != 1:
        if num == 1: break
        ans.append(prime)
        num = num / prime

if num != 1: ans.append(num)
print(ans)
