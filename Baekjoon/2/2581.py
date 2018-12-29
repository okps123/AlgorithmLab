import math

a, b = int(input()), int(input())
m, s = 10001, 0


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True


for i in range(a, b+1):
    if is_prime(i):
        s += i
        m = min(m, i)

if s > 0:
    print(s)
    print(m)
else:
    print(-1)
