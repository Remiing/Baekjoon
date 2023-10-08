# 모든 칸을 돌면서 그 칸에서 시작해서 4칸이 되는 경우 최대값을 갱신합니다.
# current_sum + max_num * (4 - cnt) < max_sum : 현재 합한 상태에서 가능한 최대값이 되어도 저장되어 있는 최대값보다 작다면 돌아갑니다.
# if cnt == 2 : 산모양의 블록을 만드는 경우입니다. 

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
max_num = max(max(p) for p in paper)
max_sum = 0

def bt(cnt, current_sum, y, x):
    global max_sum
    if cnt == 4:
        max_sum = max(max_sum, current_sum)
        return
    if current_sum + max_num * (4 - cnt) < max_sum:
        return
    for i in range(4):
        ny = y + d[i][0]
        nx = x + d[i][1]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            if cnt == 2:
                visited[ny][nx] = True
                bt(cnt + 1, current_sum + paper[ny][nx], y, x)
                visited[ny][nx] = False
            visited[ny][nx] = True
            bt(cnt + 1, current_sum + paper[ny][nx], ny, nx)
            visited[ny][nx] = False
    return

visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        bt(1, paper[i][j], i, j)
        visited[i][j] = False

print(max_sum)



