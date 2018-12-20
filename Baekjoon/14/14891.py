gears = [[] for i in range(4)]

def turn_gear(n: int, is_right: bool, d: int):
    if n > 0 and d in [0, -1]:
        if gears[n][-2]!=gears[n-1][2]:
            turn_gear(n-1, not is_right, -1)
    
    if n < 3 and d in [0, 1]:
        if gears[n][2]!=gears[n+1][-2]:
            turn_gear(n+1, not is_right, 1)

    if is_right:
        gears[n] = [gears[n][-1]]+gears[n][:-1]
    else:
        gears[n] = gears[n][1:]+[gears[n][0]]

for i in range(4):
    gears[i] = list(map(int, input()))

for i in range(int(input())):
    n, d = map(int, input().split())
    turn_gear(n-1, d>0, 0)

score = 0
for i, j in enumerate([1,2,4,8]):
    score += j if gears[i][0] == 1 else 0

print(score)