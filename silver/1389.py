import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
conn_list = [[] for _ in range(N+1)]
KB_num = [0]*(N+1)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    conn_list[a].append(b)
    conn_list[b].append(a)
for i in range(1, N+1):
    visited = [0]*(N+1)
    visited[i] = 1
    queue = [i]
    num = [0]*(N+1)
    while queue:
        point = queue.pop(0)
        for j in conn_list[point]:
            if not visited[j]:
                num[j] = num[point]+1
                queue += [j]
                visited[j] = 1
    KB_num[i] = sum(num)
print(KB_num.index(min(KB_num[1:])))
