# RGB 거리
n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
dp = [[0,0,0]]

for i in range(1, n+1):
    r = min(dp[i-1][1], dp[i-1][2]) + table[i-1][0]
    g = min(dp[i-1][0], dp[i-1][2]) + table[i-1][1]
    b = min(dp[i-1][0], dp[i-1][1]) + table[i-1][2]
    dp.append([r,g,b])

print(min(*dp[-1]))