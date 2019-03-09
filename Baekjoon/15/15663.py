def read(): return map(int, input().split())


n, m = read()
l = list(read())


def dfs(n, m, v):
    if len(v) == m:
        print(*v, sep=' ')
        return

    x = []
    for i in sorted(l):
        if not i in x:
            dfs(n, m, v+[i])
            x.append(i)


dfs(n, m, [])
