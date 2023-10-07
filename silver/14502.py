# 벽을 놓을 수 있는 조합을 모두 확인해서 최대로 안전한 넓이를 찾습니다. 

from itertools import combinations
import sys
input = sys.stdin.readline
y, x = map(int, input().split())
dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)
lab = []
virus = []
blank = []
wall_num = 3
for i in range(y):
    low = list(map(int, input().split()))
    lab.append(low)
    for j in range(x):
        if low[j] == 2:
            virus.append((i, j))
        elif low[j] == 1:
            wall_num += 1
        else:
            blank.append((i, j))


def virus_num(map_list, virus_list):
    virus_cnt = len(virus_list)
    q = virus_list
    while q:
        vy, vx = q.pop()
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < y and 0 <= nx < x and not map_list[ny][nx]:
                virus_cnt += 1
                map_list[ny][nx] = 2
                q.append((ny, nx))
    return virus_cnt


max_safe = 0
for com in combinations(blank, 3):
    new_lab = [lab[i][:] for i in range(y)]
    for wy, wx in com:
        new_lab[wy][wx] = 1
    if com_safe := (y*x-virus_num(new_lab, virus.copy())-wall_num):
        max_safe = max(max_safe, com_safe)
print(max_safe)

# 다른사람코드
# 연구실 외곽에 1로 벽을 두른 뒤 벽을 놓을 수 있는 자리(근처 8칸에 벽이 있는 경우) 리스트를 만들고 재귀로 dfs를 돌립니다.

import sys
input = sys.stdin.readline

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dir8 = dir + [(-1, -1), (-1, 1), (1, -1), (1, 1)]



N, M = map(int, input().split())
candi, virus = [], []

Map = [[1] * (M+2)]
for _ in range(N):
    Map.append([1] + list(map(int, input().split())) + [1])
Map += [[1] * (M+2)]
N, M = N + 2, M + 2

def is_wall_near(x, y):
    for dx, dy in dir8:
        if Map[y + dy][x + dx] == 1:
            return True
    return False

space_total = 0
for y in range(1, N-1):
    for x in range(1, M-1):
        if Map[y][x] == 0:
            space_total += 1
            if is_wall_near(x, y):
                candi.append((x, y))
        elif Map[y][x] == 2:
            virus.append((x, y))

min_spread = 64

def dfs(wall_count, idx, candi):
    if wall_count == 3:
        bfs()
        return

    for i in range(idx, len(candi)):
        new_candi = []
        cx, cy = candi[i]
        for dx, dy in dir8:
            nx, ny = cx + dx, cy + dy
            if Map[ny][nx] == 0 and (nx, ny) not in candi:
                new_candi.append((nx, ny))

        Map[cy][cx] = 1
        dfs(wall_count + 1, i + 1, candi + new_candi)
        Map[cy][cx] = 0

def bfs():
    global min_spread

    spread_count = 0
    visited = [[False] * M for _ in range(N)]
    for x, y in virus:
        visited[y][x] = True
    q = [] + virus

    for cx, cy in q:
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if Map[ny][nx] or visited[ny][nx]:
                continue
            spread_count += 1
            visited[ny][nx] = True
            q.append((nx, ny))

    min_spread = min(min_spread, spread_count)

dfs(0, 0, candi)
answer = space_total - 3 - min_spread
print(answer)





