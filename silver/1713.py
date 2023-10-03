# 새로운 추천이 들어오면 큐에서 값이 있는지 확인하고 있다면 추천수를 올립니다.
# 새로운 추천이 사진틀에 없는 경우 큐에 [추천수(1), 들어온순서(idx), 학생 넘버링]을 넣습니다.
# 힙큐로 인해서 자동정렬되고 최소값을 제거합니다.

import sys
import heapq
input = sys.stdin.readline
n = int(input())
b = int(input())
rcmd = list(map(int, input().split()))
q = [[0, 0, 0]]*n
for i in range(b):
    for j in range(n):
        if q[j][2] == rcmd[i]:
            q[j][0] += 1
            heapq.heapify(q)
            break
    else:
        heapq.heappop(q)
        heapq.heappush(q, [1, i, rcmd[i]])
print(*sorted([q[i][2] for i in range(n) if q[i][2]]))

# 다른사람코드
#

N = int(input())
R = int(input())
reco = list(map(int, input().split()))

picture = {}

for i in reco:
    if picture.get(i):
        picture[i] = picture[i] + 1
    else:
        if len(picture) >= N:
            del(picture[sorted(picture.items(), key=lambda x: x[1])[0][0]])
        picture[i] = 1

print(*sorted(picture.keys()))




