s = input()
while s != "0":
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s)-i-1]:
            print("no")
            break
    else:
        print("yes")

    s = input()
