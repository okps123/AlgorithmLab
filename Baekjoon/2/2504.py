import sys

def solve(line):
    s, n, m = [], 0, 1
    a, b = 0, 0

    for i in range(len(line)):
        hasNext = i+1 < len(line)

        if line[i] == '(':
            s.append(line[i])
            m *= 2
            a += 1
            if hasNext:
                if line[i+1] == ')':
                    n += m
                elif line[i+1] == ']':
                    return 0

        elif line[i] == '[':
            s.append(line[i])
            m *= 3
            b += 1
            if hasNext:
                if line[i+1] == ']':
                    n += m
                elif line[i+1] == ')':
                    return 0

        elif line[i] == ')':
            if not s: return 0
            s.pop()
            m /= 2
            a -= 1

        elif line[i] == ']':
            if not s: return 0
            s.pop()
            m /= 3
            b -= 1

    if len(s) != 0 or a != 0 or b != 0:
        return 0

    return int(n)

print(solve(sys.stdin.readline().strip()))