# Case #1: 1 + 1 = 2
# Case #2: 2 + 3 = 5
# Case #3: 3 + 4 = 7
# Case #4: 9 + 8 = 17
# Case #5: 5 + 2 = 7

for i in range(int(input())):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (i+1, a, b, a+b))
