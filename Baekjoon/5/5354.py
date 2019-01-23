def printBox(size):
  if size == 1:
    print('#')
    return

  print('#'*size)
  for i in range(size-2):
    print('#' + 'J' * (size-2) + '#')
  print('#'*size)

for i in range(int(input())):
  printBox(int(input()))
  print()