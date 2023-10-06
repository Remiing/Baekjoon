# 입력을 받을 때마다 가장 작은 값을 pop해서 가장 큰 n개의 숫자만 q에 남깁니다.

import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    for num in map(int, input().split()):
        heapq.heappush(q, num)
        if len(q) > n:
            heapq.heappop(q)
print(q[0])

# 다른사람코드
# heapreplace를 알았다. 새로 들어올 값이 heap의 가장 작은 값보다 작으면 스킵. 

def sol():
    N = int(input())
    heap = list(map(int, input().split()))
    for _ in range(N - 1):
        for i in map(int, input().split()):
            if heap[0] < i:
                heapq.heapreplace(heap, i)
    return heap[0]
print(sol())






