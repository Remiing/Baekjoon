# 문제 그대로 짠 코드입니다. dy, dx는 0일때 북쪽, 1일때 동쪽 인덱스를 가리킵니다. 

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 1
room[r][c] = 2
while True:
    for i in range(3, -1, -1):
        nd = (d + i) % 4
        ny = r + dy[nd]
        nx = c + dx[nd]
        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 0:
            room[ny][nx] = 2
            cnt += 1
            r, c, d = ny, nx, nd
            break
    else:
        ny = r - dy[d]
        nx = c - dx[d]
        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 2:
            r, c = ny, nx
        else:
            break

print(cnt)

# 다른사람코드
# 문제를 다시 보니 외곽에 벽이 있어서 0 <= ny < n and 0 <= nx < m 조건이 필요없었다.
# 항상 반시계로만 회전하기 때문에 i를 이용해 회전할 필요없이 d = (d + 3) % 4 로 회전 가능하다.

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def robot(r, c, d):
    cnt = 1
    arr[r][c] = 2
    while 1:
        for _ in range(4):
            d = (d + 3) % 4
            nr, nc = r + dr[d], c + dc[d]
            if arr[nr][nc] == 0:
                arr[nr][nc] = 2
                cnt += 1
                r, c = nr, nc
                break
        else:
            r, c = r + dr[d] * (-1), c + dc[d] * (-1)
            if arr[r][c] == 1:
                return cnt

print(robot(r, c, d))