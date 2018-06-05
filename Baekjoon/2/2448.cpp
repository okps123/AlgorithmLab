#include <stdio.h>
#define MAX_WIDTH 3072
#define MAX_HEIGHT 6200

int board[MAX_WIDTH][MAX_HEIGHT] = { 0, };

void draw_star(int n, int x, int y) {
    if(n==3) {
        board[y][x] = 1;
        board[y+1][x-1] = 1;
        board[y+1][x+1] = 1;
        for(int i = -2; i < 3; i++) {
            board[y+2][x+i] = 1;
        }
    } else {
        draw_star(n/2, x, y);
        draw_star(n/2, x-(n/2), y+(n/2));
        draw_star(n/2, x+(n/2), y+(n/2));
    }
}

int main() {
    int n;
    scanf("%d", &n);

    draw_star(n, n-1, 0);

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n*2+1; j++)
        {
            if(board[i][j] == 1) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
    
    return 0;
};

/*
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
# output
for i in range(height):
  for j in range(width):
    if board[i][j]:
      output += "*"
    else:
      output += " "

  if i < (height - 1):
    output += "\n"

print(output)
*/