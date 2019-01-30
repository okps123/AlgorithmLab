x = [False, True, False, False]
for i in range(int(input())):
  a,b=map(int,input().split())
  x[a],x[b]=x[b],x[a]

print(x.index(True))