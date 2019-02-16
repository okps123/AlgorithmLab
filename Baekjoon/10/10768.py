m, d = int(input()), int(input())
if m == 1:
    print("Before")
elif m == 2:
    if d < 18:
        print("Before")
    elif d > 18:
        print("After")
    else:
        print("Special")
elif m > 2:
    print("After")
