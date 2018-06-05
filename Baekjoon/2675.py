for i in range(int(input())):
    r, s = input().split()
    print("".join(map(lambda s: s*int(r), s)))