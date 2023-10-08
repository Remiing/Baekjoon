from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1
board[0][0] = -1

l = int(input())
timeline = [0] * 10200
for _ in range(l):
    x, c = input().split()
    timeline[int(x)] = 1 if c == 'L' else 2

d = ((-1, 0), (0, -1), (1, 0), (0, 1))
current_d = 3

snake = deque([(0, 0)])
sy, sx = 0, 0

i = 0
for i in range(1, len(timeline)):
    sy, sx = sy + d[current_d][0], sx + d[current_d][1]
    if not 0 <= sy < n or not 0 <= sx < n or board[sy][sx] == -1:
        break
    if board[sy][sx] == 0:
        board[snake[0][0]][snake[0][1]] = 0
        snake.popleft()
    board[sy][sx] = -1
    snake.append((sy, sx))
    if timeline[i]:
        current_d = (current_d + 1) % 4 if timeline[i] == 1 else (current_d + 3) % 4

print(i)






