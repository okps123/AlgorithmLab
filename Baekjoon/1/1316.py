import sys

n = int(sys.stdin.readline())
cnt = n

for i in range(n):
    word = sys.stdin.readline()

    chars = []
    current_char = None

    for c in word:
        if current_char == None or c not in chars:
            current_char = c
            chars.append(c)
        elif current_char != c and c in chars:
            cnt -= 1
            break
            
print(cnt)