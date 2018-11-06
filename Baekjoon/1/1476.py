a = list(map(int, input().split()))
b = [1, 1, 1]
c = [15,28,19]

for i in range(7980):
    if a[0]==b[0] and a[1]==b[1] and a[2]==b[2]:
        print(i+1)
        break
    
    for i in range(3):
        b[i] += 1 if b[i] < c[i] else -c[i]+1