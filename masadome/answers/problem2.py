num = 2248776129600

e = set()

now = 2
while num > 1:
    if num % now == 0:
        e.add(now)
        num /= now
    else:
        now += 1

print(' '.join(map(str, list(e))))