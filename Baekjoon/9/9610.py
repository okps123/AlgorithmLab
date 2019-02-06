a,b,c,d,e=0,0,0,0,0
for i in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        e += 1
    elif x > 0 and y > 0:
        a += 1
    elif x < 0 and y > 0:
        b += 1
    elif x < 0 and y < 0:
        c += 1
    elif x > 0 and y < 0:
        d += 1

print("Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d" % (a,b,c,d,e))