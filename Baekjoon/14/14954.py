n = int(input())
m = n

while True:
    m = sum(map(lambda x: int(x)**2, str(m)))
    if m == 1:
        print("HAPPY")
        break
    elif m == 4:
        print("UNHAPPY")
        break
