n = int(input())
dp = [0, 0]

# n-1
# n%3==0이면 n/3
# n%2==0이면 n/2

for i in range(2, n+1):
    dp.append(dp[i-1]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[-1])