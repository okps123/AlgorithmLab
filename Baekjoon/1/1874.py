e = [int(input()) for i in range(int(input()))]
s = []
r = []
n = 0

for target in e:
    while (target > n):
        n += 1
        s.append(n)
        r.append('+')

    if s[-1] != target:
        r.clear()
        r.append('NO')
        break
    
    s.pop()
    r.append('-')

print('\n'.join(r))