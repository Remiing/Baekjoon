# 우선 board를 돌면서 연속된 최대 길이를 answer에 저장합니다.
# board를 돌면서 그 자리에서 상하좌우의 값과 자신을 교체했을 때 그 자리에서의 최대값을 찾고 저장합니다. 

import sys
input = sys.stdin.readline
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        y, x = i, j
        while x < n and board[i][j] == board[i][x]:
            x += 1
        while y < n and board[i][j] == board[y][j]:
            y += 1
        answer = max(answer, y - i, x - j)

for i in range(n):
    for j in range(n):
        for y, x in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
            if 0 <= y < n and 0 <= x < n and board[i][j] != board[y][x]:
                board[i][j], board[y][x] = board[y][x], board[i][j]
                y1, y2 = i, i
                while 0 <= y1 and board[i][j] == board[y1][j]:
                    y1 -= 1
                while y2 < n and board[i][j] == board[y2][j]:
                    y2 += 1
                x1, x2 = j, j
                while 0 <= x1 and board[i][j] == board[i][x1]:
                    x1 -= 1
                while x2 < n and board[i][j] == board[i][x2]:
                    x2 += 1
                answer = max(answer, y2 - y1 - 1, x2 - x1 - 1)
                board[i][j], board[y][x] = board[y][x], board[i][j]
print(answer)










