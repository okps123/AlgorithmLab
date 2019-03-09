def read(): return map(int, input().split())


n, m = read()
l = list(read())


def dfs(n, m, v):
    if len(v) == m:
        print(*v, sep=' ')
        return

    for i in sorted(l):
        dfs(n, m, v+[i])


dfs(n, m, [])
