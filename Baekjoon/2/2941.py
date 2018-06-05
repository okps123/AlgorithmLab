croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

n = input()
c = 0

for i in range(len(n)):
    for j in croatia:
        if j in n:
            n = n.replace(j, "@", 1)
            break

c += len(n)
print(c)