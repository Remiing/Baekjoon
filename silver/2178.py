import sys
input = sys.stdin.readline
N,M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]

queue = [(0,0)]
while queue:
    x,y = queue.pop(0)
    for nx, ny in [(x-1,y), (x,y-1), (x+1,y), (x,y+1)]:
        if 0<=nx<N and 0<=ny<M and maze[nx][ny]=='1' :
            maze[nx][ny] = int(maze[x][y]) + 1
            queue.append((nx,ny))
print(maze[N-1][M-1])

