for i in range(int(input())):
    x = 0
    for j in input():
        x+=1 if j=='(' else -1
        if x+1 <= 0: break
        
    print("YES" if x == 0 else "NO")