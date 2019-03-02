n, l = map(int, input().split())
fruits = list(sorted(map(int, input().split())))
length = l

for i in range(n):
  eatable = list(filter(lambda x: x <= length, fruits))
  if len(eatable) == 0:
    print(length)
    break 
  else:
    fruits.remove(eatable[0])
    length += 1
else:
  print(length)