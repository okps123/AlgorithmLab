a,b=0,0
for i in range(int(input())):
    c,d=map(int,input().split())
    if(c>d):
        a+=1
    elif(d>c):
        b+=1
print(a,b)