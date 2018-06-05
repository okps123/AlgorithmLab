n = int(input())

s = 1
c = 0

while s < n:
    c += 1
    s += (c * 6)

# 일반항(계차수열의 합)
# a = 1+(n*(2+n-1)*6)/2

print(s)
