d = {}
s = input().lower()

for i in s:
    d[i] = (d[i]+1 if d.get(i) else 1)

max_score = max(d.values())
items = list(filter(lambda item: item[1] == max_score, d.items()))

if len(items) == 1:
    print(items[0][0].upper())
else:
    print("?")
