for i in range(int(input())):
    a, b = map(int, input().split())
    print('You get ' + str(a//b) +
          ' piece(s) and your dad gets ' + str(a % b) + ' piece(s).')
