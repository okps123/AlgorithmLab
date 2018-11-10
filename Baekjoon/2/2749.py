dp = [0 for i in range(1000000000000000000)]
def fibo(n):
    if n < 2: return n
    if dp[n] != 0: return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(int(input())))