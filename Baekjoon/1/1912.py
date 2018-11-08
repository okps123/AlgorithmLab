# 연속합
N = int(input())
data = list(map(int, input().split()))
dp = [data[0]]

# dp[i]는 0~i까지 최대 연속합
# dp[i]= MAX(dp[i], dp[i-1]+dp[i])

for i in range(1, len(data)):
    dp.append(max(data[i], dp[i-1]+data[i]))

print(max(dp))