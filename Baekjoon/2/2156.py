n = int(input())
m = [0] + [int(input()) for i in range(n)]

def solve(n, m):
    if n < 1: return 0
    elif n < 3: return sum(m)

    dp = [0 for i in range(n+1)]
    dp[1] = m[1]
    dp[2] = m[1]+m[2]

    for i in range(3, n+1):
        dp[i] = max(
            dp[i-3] + m[i-1] + m[i],
            dp[i-2] + m[i],
            dp[i-1]
        )

    return dp[-1]

print(solve(n, m))