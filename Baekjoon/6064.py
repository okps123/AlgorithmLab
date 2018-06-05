# T = int(input())
# for _ in range(T):
#     m, n, x, y = map(int, input().split())
#     i, j = 0, 0
#     c = 0

#     while True:
#         i = 1 if i >= m else (i+1)
#         j = 1 if j >= n else (j+1)
#         c += 1

#         if i == x and j == y:
#             print(c)
#             break
#         elif i == m and j == n:
#             print(-1)
#             break

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