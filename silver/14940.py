# BFS

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
distance = [[-1]*m for _ in range(n)]

x, y = 0, 0
map_list = []
for i in range(n):
    row = list(map(int, input().split()))
    map_list.append(row)
    if 2 in row:
        x = row.index(2)
        y = i

distance[y][x] = 0
queue = [(y, x)]
while queue:
    i, j = queue.pop(0)
    for ni, nj in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
        if 0 <= ni < n and 0 <= nj < m and distance[ni][nj] == -1 and map_list[ni][nj] == 1:
            distance[ni][nj] = distance[i][j] + 1
            queue.append((ni, nj))

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 0:
            distance[i][j] = 0

for i in distance:
    print(*i)

