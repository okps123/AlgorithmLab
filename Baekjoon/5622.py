buttons = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def get_num(char):
    for index, value in enumerate(buttons):
        if char in value:
            return (index + 2)

t = 0
for n in map(get_num, input()):
    t += (n + 1)

print(t)