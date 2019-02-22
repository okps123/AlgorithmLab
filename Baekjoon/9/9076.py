for i in range(int(input())):
    scores = sorted(map(int, input().split()))[1:4]
    print("KIN" if abs(scores[0]-scores[2]) >= 4 else sum(scores))
