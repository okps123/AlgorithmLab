def hanoi(n, s, m, e):
    if n == 1:
        print(s,"->", e)
    else:
        hanoi(n-1, s, e, m)
        hanoi(1, s, m, e)

n = 5

hanoi(5, "s", "m", "e")