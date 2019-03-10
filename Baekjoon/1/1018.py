n, m = map(int, input().split())
b = [list(map(lambda c: 0 if c == 'W' else 1, input())) for i in range(n)]

l = 64


def calc(r, c, low):
    na, nb = 0, 0

    # 0,0이 흰색인 체스판
    for i in range(0, 8):
        for j in range(0, 8):
            if b[r+i][c+j] != (j + (0 if (i+1) % 2 else 1)) % 2:
                na += 1

     # 0,0이 검정색인 체스판
    for i in range(0, 8):
        for j in range(0, 8):
            if b[r+i][c+j] != (j + (0 if i % 2 else 1)) % 2:
                nb += 1

    return min(na, nb)


for r in range(n-7):
    for c in range(m-7):
        l = min(l, calc(r, c, l))

print(l)
