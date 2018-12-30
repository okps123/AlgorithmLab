n = int(input())
dp = [[0 for i in range(10)] for i in range(1001)]
dp[1] = [1]*10

for i in range(2, n+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

print(sum(dp[n])%10007)
