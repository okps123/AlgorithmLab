def insertion_sort(nums: list):
    for i in range(1, len(nums)):
        j = i
        current_value = nums[i]

        while j > 0 and current_value < nums[j-1]:
            j -= 1

        # Python에서 리스트 슬라이스를 대입하는 코드는 C에서 동작
        # 해당 아이템을 반복문으로 일일이 바꾸는 것보다 빠름
        nums[j+1:i+1] = nums[j:i]
        nums[j] = current_value

    return nums

print([3,2,1,5,7,2,1], insertion_sort([3,2,1,5,7,2,1]))
