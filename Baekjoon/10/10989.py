# Counting Sort
import sys

MAX_NUM = 10000

counter = [0 for i in range(MAX_NUM+1)]
for i in range(int(sys.stdin.readline())):
    counter[int(sys.stdin.readline())] += 1

for i in range(MAX_NUM+1):
    for j in range(counter[i]):
        sys.stdout.write(str(i) + '\n')