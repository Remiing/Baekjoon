# 간단하게 dfs를 통해 붙어있는 쓰레기의 개수를 세고, 최대값을 저장한다.

import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
trash = [[False]*m for _ in range(n)]
for _ in range(k):
    y, x = map(int, input().split())
    trash[y-1][x-1] = True

answer = 0
for i in range(n):
    for j in range(m):
        if trash[i][j]:
            cnt = 1
            q = [(i, j)]
            trash[i][j] = False
            while q:
                y, x = q.pop()
                for ny, nx in [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]:
                    if 0 <= ny < n and 0 <= nx < m and trash[ny][nx]:
                        q.append((ny,nx))
                        cnt += 1
                        trash[ny][nx] = False
            answer = max(answer, cnt)

print(answer)












