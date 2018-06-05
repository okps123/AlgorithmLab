apartment = {}

def get_count(y, x):
    if y == 0:
        return x
    elif (y, x) in apartment:
        return apartment.get((y, x))
    else:
        n = sum([get_count(y-1, i+1) for i in range(x)])
        apartment[(y, x)] = n
        
        return n

N = int(input())

for i in range(N):
    x = int(input())
    y = int(input())

    print(get_count(x, y))