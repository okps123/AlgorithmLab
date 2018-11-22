n = int(input())

m = [0] + [int(input()) for i in range(n)]
dp = [[0, 0] for i in range(n+1)]
dp[1] = [m[1], m[1]]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] + m[i]
    dp[i][1] = max(dp[i-2]) + m[i]

print(max(dp[-1]))