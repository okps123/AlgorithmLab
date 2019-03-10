n = int(input())
m = int(input())

# min, sum
x, y = 100000, 0
for i in range(1, 101):
  z = i * i
  if (z >= n and z <= m):
    if (x > z):
      x = z
    y += z

if (y == 0):
  print(-1)
else:
  print(y, x, sep='\n')

