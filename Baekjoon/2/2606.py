from collections import deque

n, m = int(input()), int(input())
adj = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]

q = deque()
q.append(1)

visited[1] = True

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

l = 0
while q:
    v = q.popleft()
    for nv in adj[v]:
        if not visited[nv]:
            visited[nv] = True
            q.append(nv)
            l += 1

print(l)
