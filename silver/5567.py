from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

relation = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

answer = 0
visited = [False] * (n+1)
visited[1] = True
q = deque([(1, 0)])
while q:
    p, cnt = q.popleft()
    for friend in relation[p]:
        if not visited[friend]:
            answer += 1
            if cnt + 1 < 2:
                q.append((friend, cnt + 1))
            visited[friend] = True
print(answer)

# 다른사람코드
# bfs를 하는것보다 단순히 거리가 2인 노드의 개수를 세는 것이기 때문에 2중 for문으로만 탐색하고 방문한 노드를 세줍니다. 

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
friends = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

if not arr[1]:
    print(0)
else:
    for i in arr[1]:
        friends[i] = 1
        for j in arr[i]:
            friends[j] = 1
    print(friends.count(1) - 1)

