# 2108번 통계학
from collections import Counter
import math

n = int(input())
datas = []

for _ in range(n):
    datas.append(int(input()))

average = round(sum(datas)/len(datas))
middle = sorted(datas)[len(datas)//2]

counter = Counter(datas)
modes = counter.most_common()

ordered = sorted(map(lambda x: x[0], 
    filter(lambda x: x[1] == modes[0][1], modes)))

mode = ordered[0] if len(ordered) == 1 else ordered[1]

range_datas = abs(max(datas) - min(datas))

print(average)
print(middle)
print(mode)
print(range_datas)
