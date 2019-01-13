import sys
s, i = input(), 0
while i < len(s):
    i += 2 if s[i] in ['a', 'e', 'i', 'o', 'u'] else 0
    sys.stdout.write(s[i])
    i += 1
