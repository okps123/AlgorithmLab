line = ''
while True:
    line = input()
    if line == 'END': break
    print(''.join(reversed(line)))