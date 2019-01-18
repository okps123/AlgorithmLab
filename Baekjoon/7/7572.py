n = (int(input())%60)-3
print("%s%d"%("ABCDEFGHIJKL"[((n-1) % 12)],(n-1)%10))