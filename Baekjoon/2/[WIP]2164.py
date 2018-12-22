n = int(input())
m = [i for i in range(1,n+1)]

while len(m) > 1:
    m.remove(m[0])
    t = m[0]
    m.remove(m[0])
    m.append(t)

print(m[0])