from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
adj = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)


def dfs(v):
    visited = [False for i in range(n+1)]
    stack = deque()
    stack.append(v)

    cnt = 0

    while stack:
        v = stack.pop()
        visited[v] = True
        cnt += 1

        for nv in adj[v]:
            if not visited[nv]:
                stack.append(nv)

    return cnt


ans = [0 for i in range(n+1)]
maxCnt = 0
for i in range(n+1):
    ans[i] = dfs(i)
    maxCnt = max(maxCnt, ans[i])

for i in range(n+1):
    if ans[i] == maxCnt:
        sys.stdout.write(str(i) + " ")

sys.stdout.write('\n')
