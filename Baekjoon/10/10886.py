n = int(input())  # 1, 3, 5
m = [int(input()) for i in range(n)]
print("Junhee is" + ("" if sum(m) > n//2 else " not") + " cute!")
