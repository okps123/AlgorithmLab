n, w, h = map(int, input().split())

for i in range(n):
    x = int(input())
    print('DA' if (x**2 <= (w**2+h**2)) else 'NE')