for i in range(int(input())):
    s = input()
    s = str(int(s) + int(s[::-1]))
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            print("NO")
            break
    else:
        print("YES")
