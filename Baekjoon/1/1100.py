board = "".join([input() for i in range(8)])
count = 0

for i in range(8):
  for j in range(4):
    count += 1 if board[i*8+(j*2)+(1 if (i+1)%2==0 else 0)] == 'F' else 0

print(count)