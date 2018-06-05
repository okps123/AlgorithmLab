import sys

n = int(input())

width = int(n/3)*6+1
height = n

board = [[False for i in range(width)] for j in range(height)]

def draw_star(n, x, y):
  if n == 3:
    board[y][x] = True
    board[y+1][x-1] = True
    board[y+1][x+1] = True
    board[y+2][x-2] = True
    board[y+2][x-1] = True
    board[y+2][x] = True
    board[y+2][x+1] = True
    board[y+2][x+2] = True
  else:
    draw_star(n/2, x, y)
    draw_star(n/2, x-int(n/2), y+int(n/2))
    draw_star(n/2, x+int(n/2), y+int(n/2))
  
draw_star(n, int(width/2)-1, 0)

output = ""

for i in range(height):
  for j in range(width):
    if board[i][j]:
      output += "*"
    else:
      output += " "

  if i < (height - 1):
    output += "\n"

print(output)