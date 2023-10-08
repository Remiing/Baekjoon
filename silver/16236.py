# 처음 상어의 위치부터 먹을 수 있는 물고기를 만날때까지 bfs를 돌립니다. 만약 같은 거리의 물고기가 여러마리라면 가장 왼쪽 위의 물고기의 위치와 거리를 리턴합니다. 

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
space = []
for i in range(n):
    row = list(map(int, input().split()))
    space.append(row)
    for j in range(n):
        fish_size = row[j]
        if fish_size == 9:
            sy, sx = i, j

shark = 2
shark_level = 0
time = 0
space[sy][sx] = 0

d = ((-1, 0), (0, -1), (1, 0), (0, 1))
def find_fish(y, x, shark_size):
    visited = [[False]*n for _ in range(n)]
    visited[y][x] = True
    q = deque([(y, x, 0)])
    fish = []
    distance = 500
    while q:
        cy, cx, cnt = q.popleft()
        if cnt >= distance:
            break
        for dy, dx in d:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and space[ny][nx] <= shark_size:
                if 0 < space[ny][nx] < shark_size:
                    distance = cnt + 1
                    fish.append((ny, nx, cnt + 1))
                else:
                    q.append((ny, nx, cnt + 1))
                    visited[ny][nx] = True
    if fish:
        return sorted(fish)[0]
    return False


while near_fish := find_fish(sy, sx, shark):
    sy, sx = near_fish[0], near_fish[1]
    time += near_fish[2]
    shark_level += 1
    space[sy][sx] = 0
    if shark == shark_level:
        shark += 1
        shark_level = 0

print(time)