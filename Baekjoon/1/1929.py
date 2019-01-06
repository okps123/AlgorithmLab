n, m = map(int, input().split())
a = [True for i in range(m+1)]
a[1] = False

for i in range(2, m+1):
    if a[i]:
        for j in range(i*i, m+1, i):
            a[j] = False

print(*[i for i in range(n, m+1) if a[i]], sep='\n')
