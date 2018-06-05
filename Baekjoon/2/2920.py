array = list(map(int, input().split()))
is_ascending = ((array[1] - array[0]) == 1)

for i in range(0, len(array)-1):
    d = (array[i+1] - array[i])
    if (d != (1 if is_ascending else -1)):
        print("mixed")
        break
else:
    print("ascending" if is_ascending else "descending")