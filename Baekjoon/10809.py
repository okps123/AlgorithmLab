array = [-1 for i in range(26)]
input = input()

for i in range(len(input)):
    idx = ord(input[i]) - 97
    if array[idx] == -1:
        array[idx] = i

print(" ".join(map(str, array)))