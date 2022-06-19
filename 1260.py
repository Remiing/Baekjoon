import sys
N, M, V = map(int, sys.stdin.readline().rstrip().split())
con_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    con_list[a].append(b)
    con_list[b].append(a)


def DFS(con_list, V):
    visited = []
    stack = [V]
    while stack:
        point = stack.pop()
        if point not in visited:
            stack.extend(sorted(con_list[point], reverse=True))
            visited.append(point)
    return visited


def BFS(con_list, V):
    visited = []
    queue = [V]
    while queue:
        point = queue.pop(0)
        if point not in visited:
            queue.extend(sorted(con_list[point]))
            visited.append(point)
    return visited

print(*DFS(con_list, V), sep=' ')
print(*BFS(con_list, V), sep=' ')
        
