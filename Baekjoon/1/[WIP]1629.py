def fpow(a, n):
    if n == 0: return 1
    if n == 1: return a
    p = fpow(a, int(n/2))
    if n % 2 == 0:
        return p*p
    else:
        return p*p*a

x, y = map(int, input().split())
a = fpow(x, y)
b = pow(x, y)

print(a, b, a==b, sep='\n')