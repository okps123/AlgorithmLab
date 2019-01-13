try:
    while True:
        print(sum(map(int, input().split())))
except EOFError:
    exit()
