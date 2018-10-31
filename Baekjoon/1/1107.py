import sys

n, m, l = int(sys.stdin.readline()), int(sys.stdin.readline()), []
if m > 0: l = list(map(int, sys.stdin.readline().split()))[:m]

def is_inputtable(v:int):
    for i in str(v):
        if int(i) in l: return False
    return True

distance = 9999999
value = 0

# n보다 작지만 최대한 큰 채널에서 가는 경우
for i in range(n-1, -1, -1):
    if is_inputtable(i) and abs(n-i) < distance:
        distance, value = abs(n-i), i
        break

# n보다 크지만 최대한 작은 채널에서 가는 경우
for i in range(n, 1000001):
    if is_inputtable(i) and abs(n-i) < distance:
        distance, value = abs(n-i), i
        break

r1 = len(str(value)) + distance
r2 = abs(100-n)

print(min(r1, r2))