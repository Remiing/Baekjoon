# 문제 자체는 어려울게 없었는데 고려할게 많아서 모든 노드를 탐색하다보니 시간초과가 난다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
com_dict = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    com_dict[b].append(a)

def bfs(com_num):
    cnt = 1
    visited = [0] * (n + 1)
    visited[com_num] = 1
    q = [com_num]
    while q:
        num = q.pop()
        for cn in com_dict[num]:
            if not visited[cn]:
                q.append(cn)
                visited[cn] = 1
                cnt += 1
    return cnt

maxnum = 0
nlist = list(range(n+1))
for i in range(1, n+1):
    nlist[i] = bfs(i)
    maxnum = max(maxnum, nlist[i])

for i in range(1, n+1):
    if nlist[i] == maxnum:
        print(i, end=' ')
