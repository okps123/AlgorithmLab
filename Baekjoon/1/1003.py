dp = [0 for i in range(41)]
def fibo(n):
    if n < 2: return n
    if dp[n] != 0: return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

for i in range(int(input())):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        print("%d %d" % (fibo(n-1), fibo(n)))