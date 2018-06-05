arr = [0 for i in range(10)]

for i in input():
    n = int(i)
    if n in [6, 9]:
        arr[9 if arr[6] >= arr[9] else 6] += 1
    else:
        arr[n] += 1

print(max(arr))