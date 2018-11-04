n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

def dfs(i, current_sum):
    global nums, cnt

    if i >= len(nums): return
    if (current_sum + nums[i]) == s: cnt += 1

    dfs(i+1, current_sum)
    dfs(i+1, current_sum + nums[i])

dfs(0, 0)

print(cnt)