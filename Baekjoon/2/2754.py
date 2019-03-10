g, s = ['F', 'D', 'C', 'B', 'A'], 0.0
for c in input():
    s += g.index(c) if c in g else 0
    s += 0.3 if c == '+' else (-0.3 if c == '-' else 0)
print(s)
