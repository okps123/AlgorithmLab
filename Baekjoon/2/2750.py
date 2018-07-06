# 2750번 수 정렬하기

datas = []
for i in range(int(input())):
    datas.append(int(input()))

# 버블 정렬

# length = len(datas) - 1

# for i in range(length):
#     for j in range(length - i):
#         if datas[j] > datas[j+1]:
#             datas[j], datas[j+1] = datas[j+1], datas[j]

# 선택 정렬

length = len(datas)

for i in range(length):
    min_index = i

    for j in range(i, length):
        if datas[j] < datas[min_index]:
            min_index = j
    
    datas[i], datas[min_index] = datas[min_index], datas[i]

for i in datas:
    print(i)