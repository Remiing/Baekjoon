import sys
import time
N, M = map(int, sys.stdin.readline().rstrip().split())
start = time.time()
count = 0
visited = [0]*100001
visited[N] = 1
queue = [N, -1]
while queue:
    point = queue.pop(0)
    if point == -1:
        queue += [-1]
        count += 1
        continue
    if point == M:
        break
    for i in [point-1, point+1, point*2]:
        if 0<=i<=100000 and not visited[i]:
            queue += [i]
            visited[i] = 1
print(count)

#else coed
def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)
  
import sys
n, k = map(int, sys.stdin.readline().split())
print(find(n, k))
