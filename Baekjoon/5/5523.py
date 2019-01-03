import sys

a,b=0,0
for i in range(int(sys.stdin.readline())):
    c,d=map(int,sys.stdin.readline().split())
    if(c>d):
        a+=1
    elif(d>c):
        b+=1
print(a,b)