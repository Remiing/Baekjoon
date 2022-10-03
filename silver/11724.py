import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
connect_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    connect_list[u].append(v)
    connect_list[v].append(u)
count = 0
visited = [0 for _ in range(N+1)]
for i in range(1,N+1):
    if not visited[i]:
        count += 1
        queue = [i]
        while queue:
            point = queue.pop(0)
            for j in connect_list[point]:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = 1
print(count)
