n = int(input())
m = []
dp = [[0 for i in range(j)] for j in range(1, n+1)]

for i in range(n):
    m.append(list(map(int, input().split())))

dp[0][0] = m[0][0]

for i in range(1, len(m)):
    for j in range(len(m[i])):
        if j == 0:
            dp[i][j] = m[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = m[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = m[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[-1]))