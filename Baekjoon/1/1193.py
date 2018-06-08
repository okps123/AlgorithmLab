# 1193번 분수 찾기

def solve(x):
    s, n = 0, 0

    while True:
        n += 1
        s += n
        if x <= s:
            break

    is_even = (n % 2 == 0)
    p = int(sum([i for i in range(1, n + (0 if is_even else 1))])) + (1 if is_even else 0)
    
    a, b = 1, n
    for i in range(abs(x-p)):
        a += 1
        b -= 1

    return "%d/%d" % (a,b)

print(solve(int(input())))