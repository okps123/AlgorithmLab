n = int(input())
origin = input()

for i in range(n-1):
  s = input()
  for j in range(len(s)):
    if origin[j] != '?' and s[j] != origin[j]:
      origin = origin[:j] + '?' + origin[j+1:]

print(origin)