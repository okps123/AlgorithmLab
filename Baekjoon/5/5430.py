import sys

for i in range(int(sys.stdin.readline())):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    x = list(sys.stdin.readline().rstrip('\n')[1:-1].split(','))

    if len(x) == 1 and x[0] == '':
        sys.stdout.write('error\n')
        continue

    for c in p:
        try:
            if c == 'R':
                x.reverse()
            elif c == 'D':
                del x[0]
                n -= 1
        except:
            sys.stdout.write('error\n')
            break
    else:
        sys.stdout.write('[')
        for j in range(len(x)-1):
            sys.stdout.write(x[j]+',')
        sys.stdout.write(x[-1] + ']\n')

