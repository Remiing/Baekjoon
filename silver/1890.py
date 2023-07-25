# 처음에 bfs로 풀었는데 dp로 풀면 100x100의 보드판을 모두 돌면서 푸는 것보다 bfs의 queue를 활용해서 건너뛰며 계산하는 것이 더 효율적이라고 생각했다.
# 하지만 bfs로 풀었을때 만약 모든 항이 1이라면 queue에 2개씩 대기열이 쌓이다보니 메모리초과가 생기는 문제가 있었다.

import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
count = [[0]*n for _ in range(n)]
count[0][0] = 1
for y in range(n):
    for x in range(n):
        value = board[y][x]
        if not value or not count[y][x]: continue
        nx, ny = x+value, y+value
        if nx<n:
            count[y][nx] += count[y][x]
        if ny<n:
            count[ny][x] += count[y][x]
print(count[-1][-1])

# 다른사람코드
#

n,*a=map(int,open(0).read().split())
b=[1]+[0]*n*n
for i in range(n):
 for j in range(n):
  k=i*n+j;d=a[k];e=b[k]
  if(d>0)*(e>0):
   if i+d<n:b[k+d*n]+=e
   if j+d<n:b[k+d]+=e
print(b[-2])


