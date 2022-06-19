import sys
T = int(sys.stdin.readline().rstrip())
x_axis = [1, 0, -1, 0]
y_axis = [0, 1, 0, -1]
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().rstrip().split())
    count = 0
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        field[x][y] = 1
    for x in range(N):
        for y in range(M):
            if field[x][y]==1:
                count += 1
                queue = [[x,y]]
                field[x][y] = 0
                while queue:
                    xq, yq = queue.pop(0)
                    for i in range(4):
                        a = xq + x_axis[i]
                        b = yq + y_axis[i]
                        if 0<=a<N and 0<=b<M and field[a][b]==1:
                            queue.append([a,b])
                            field[a][b] = 0
    print(count)


#다른사람풀이 
import sys
I=sys.stdin.readline
def f(i,j):
    q=[(i,j)]
    while q:
        i,j=q.pop()
        g[i][j]=0
        for i,j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if i>-1 and i<n and j>-1 and j<m and g[i][j]:q+=[[i,j]]
J=lambda:map(int,I().split())
for _ in[0]*int(I()):
    c=0
    n,m,k=J()
    g=[[0]*m for i in[0]*n]
    for i in[0]*k:v,w=J();g[v][w]=1
    for i in range(n):
        while any(g[i]):f(i,g[i].index(1));c+=1
    print(c)
