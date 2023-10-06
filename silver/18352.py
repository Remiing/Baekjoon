from collections import deque
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())

road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)

answer = []
visited = [False]*(n+1)
visited[x] = True
q = deque([(x, 0)])
while q:
    city, cnt = q.popleft()
    for connect_city in road[city]:
        if not visited[connect_city]:
            if cnt + 1 < k:
                q.append((connect_city, cnt + 1))
            else:
                answer.append(connect_city)
            visited[connect_city] = True
if answer:
    print(*sorted(answer), sep='\n')
else:
    print(-1)









