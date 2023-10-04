import sys
input = sys.stdin.readline
n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
cnt = 0
q = [(t1, 0)]
while q:
    t, cnt_tmp = q.pop()
    for nt in relation[t]:
        if nt == t2:
            print(cnt_tmp + 1)
            exit()
        if not visited[nt]:
            visited[nt] = True
            q.append((nt, cnt_tmp + 1))
print(-1)










