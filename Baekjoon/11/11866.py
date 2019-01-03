from queue import Queue

n, m = map(int, input().split())
s, r = Queue(), []

c = 0

for i in range(1, n+1):
    s.put(i)

while not s.empty():
    a = s.get()
    c += 1
    if c != m:
        s.put(a)
    else:
        c = 0
        r.append(str(a))

print("<" + ", ".join(r) + ">")
