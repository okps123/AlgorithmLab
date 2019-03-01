def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

for i in range(int(input())):
  a,b = map(int, input().split())
  print(int(a*b/gcd(a,b)))