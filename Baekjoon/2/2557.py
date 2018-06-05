# 2577 Counting Number

counter = [0 for i in range(10)]

a = int(input())
b = int(input())
c = int(input())

for i in str(a*b*c):
    counter[int(i)] += 1

for i in range(10):
    print(counter[i])