from queue import Queue

for t in range(int(input())):
    q = Queue()

    n, m = map(int, input().split())
    for i in map(int, input().split()):
        q.put(i)

    c = 0
    while not q.empty():
        x = q.get()

        if any(map(lambda i: i > x, q.queue)):
            m += len(q.queue) if m == 0 else -1
            q.put(x)
        else:
            if m == 0:
                print(c+1)
                break
            c += 1
            m -= 1


