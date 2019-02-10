x = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    x += b % a

print(x)
