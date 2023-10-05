# 미로를 돌면서 자기 위치 기준 오른쪽, 위쪽, 오른쪽위대각 중 가장 큰 값에 자기 방의 사탕을 더해 자기 값을 갱신합니다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [[0]*(m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m+1):
        maze[i][j] += max(maze[i-1][j], maze[i][j-1], maze[i-1][j-1])
print(maze[n][m])

# 다른사람코드
#

n, m, *a = map(int, open(0).read().split())
b = [0]*m
for i in range(n):
    p = 0
    b = [p := max(p, d)+c for c, d in zip(a[i*m:i*m+m], b)]
    print(b)
print(p)




