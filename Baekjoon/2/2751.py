# 2751번 수 정렬하기 2
# 병합 정렬(Merge Sort), 힙 정렬(Heap Sort) 구현
# Pypy3로 채점
import sys

def merge(left, right):
    sorted_list = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

def merge_sort(datas):
    if len(datas) == 1:
        return datas
    
    mid = len(datas) // 2

    left = merge_sort(datas[:mid])
    right = merge_sort(datas[mid:])

    return merge(left, right)

datas = []
for i in range(int(sys.stdin.readline())):
    datas.append(int(sys.stdin.readline()))

for i in merge_sort(datas):
    sys.stdout.write(str(i) + '\n')