# 피보나치 수 3

# 솔루션
# 피사노 주기: 피보나치 수를 K로 나눈 나머지는 같은 주기를 갖는다.
# 주기의 길이가 P이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
# M=10^k (k>2)이면 주기는 15*10^(k-1)이다.

n = int(input())
m = 1000000
p = int(m/10*15)

fibo = [0, 1]

for i in range(2, p):
    fibo.append((fibo[i-1] + fibo[i-2]) % m)

print(fibo[n%p])