# 간단하게 bfs로 보드판의 각 칸을 몇번만에 이동할 수 있는지 계산

import sys
input = sys.stdin.readline
n = int(input())
move = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def knight():
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end: return 0
    board = [[-1]*l for _ in range(l)]
    board[start[1]][start[0]] = 0
    queue = [start]
    while queue:
        x, y = queue.pop(0)
        for move_x, move_y in move:
            mx = x + move_x
            my = y + move_y
            if end == (mx, my): return board[y][x] + 1
            if 0 <= mx < l and 0 <= my < l and board[my][mx] == -1:
                board[my][mx] = board[y][x] + 1
                queue += [(mx, my)]

for _ in range(n):
    print(knight())

# 다른사람코드
#
t = int(input())
score = {(0, 0): 0, (0, 1): 3, (0, 2): 2, (0, 3): 3, (0, 4): 2, (1, 1): 2, (1, 2): 1, (1, 3): 2, (1, 4): 3,
         (2, 2): 4, (2, 3): 3, (2, 4): 2, (3, 3): 2, (3, 4): 3, (4, 4): 4}
for _ in range(t):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    i, j = abs(a - c), abs(b - d)
    i, j = min(i, j), max(i, j)
    cnt = 0
    print(i, j)
    while j > 4:
        if i:
            i -= 1
        else:
            i = 1
        j -= 2
        if i > j:
            i, j = j, i
        print(i, j)
        cnt += 1
    corner = {(0, 0), (0, l - 1), (l - 1, 0), (l - 1, l - 1)}
    cnt += score[(i, j)]
    if (a, b) in corner or (c, d) in corner:
        if (i, j) == (1, 1):
            cnt = 4
        elif (min(abs(a - c), abs(b - d)), max(abs(a - c), abs(b - d))) == (0, 3) and l == 4:
            cnt = 5
    print(cnt)
