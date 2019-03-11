def read(): return map(int, input().split())


def dfs(n, m, v, u):
    if len(v) == m:
        print(*v, sep=' ')
        return

    us = []
    for i in sorted(u):
        if i in us:
            continue
        us += [i]
        dfs(n, m, v+[i], u[:u.index(i)]+u[u.index(i)+1:])


n, m = read()
dfs(n, m, [], list(read()))
