n, m = int(input()), [1, 1]
for i in range(1,n-1):
    m.append(m[i]+m[i-1])

print(m[-1])