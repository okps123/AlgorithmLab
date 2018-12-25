from queue import Queue

n, m, v = map(int, input().split())
a = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    a[v1][v2] = a[v2][v1] = 1


def dfs(a, c, v):
    c[v] = 1
    print(v, end=' ')

    for i in range(len(a[v])):
        if a[v][i] == 1 and c[i] == 0:
            dfs(a, c, i)


def bfs(a, c, v):
    q = Queue()
    q.put(v)

    c[v] = 1

    while not q.empty():
        v = q.get()
        print(v, end=' ')

        for i in range(len(a[v])):
            if a[v][i] == 1 and c[i] == 0:
                q.put(i)
                c[i] = 1


dfs(a, [0 for i in range(n+1)], v)

print()

bfs(a, [0 for i in range(n+1)], v)
