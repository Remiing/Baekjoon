import sys
input = sys.stdin.readline
board = [input().split() for _ in range(19)]
for i in range(19):
    for j in range(19):
        if board[i][j] != '0':
            for dy, dx in [(-1, 1), (0, 1), (1, 1), (1, 0)]:
                y0, y1, y2, y3, y4, y5 = i - dy, i + dy, i + dy*2, i + dy*3, i + dy*4, i + dy*5
                x0, x1, x2, x3, x4, x5 = j - dx, j + dx, j + dx*2, j + dx*3, j + dx*4, j + dx*5
                if 0 <= y4 < 19 and 0 <= x4 < 19 and board[i][j] == board[y1][x1] == board[y2][x2] == board[y3][x3] == board[y4][x4]:
                    if 0 <= y5 < 19 and 0 <= x5 < 19 and board[i][j] == board[y5][x5]:
                        continue
                    if 0 <= y0 < 19 and 0 <= x0 < 19 and board[i][j] == board[y0][x0]:
                        continue
                    print(board[i][j])
                    print(i+1, j+1)
                    exit()
print(0)










