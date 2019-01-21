n = [[l for l in input()] for i in range(5)]
for i in range(15):
    for j in range(5):
        if i >= len(n[j]): continue
        print(n[j][i], end='')