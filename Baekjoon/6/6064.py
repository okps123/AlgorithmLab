# 6064번 카잉 달력

def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return a * b / get_gcd(a, b)

m, n, x, y = map(int, input().split())

if m > n:
    m, n, x, y = n, m, y, x

c = x
for i in range(int(get_lcm(m,n)/m)):
    l = (m * i) + x
    b = l % n

    if c == y:
        print(l)
        break

    c -= (n-m)
    if c <= 0:
        c += n
    
else:
    print(-1)