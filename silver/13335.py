# 간단하게 deque를 놓고 현재 다리위(deque)에 새로운 트럭을 추가했을 때 L보다 작으면 트럭을 다리 위로 올립니다.
# 아직 다리를 건너지 못한 트럭이나 다리 위에 트럭이 남아있다면 pop, append를 통해 한 칸씩 이동시킵니다.

from collections import deque
import sys
input = sys.stdin.readline
# n, w, l = map(int, input().split())
# trucks = list(map(int, input().split()))[::-1]
# bridge = deque([0]*w)
# time = 0
# weight = 0
# while trucks or weight:
#
#     weight -= bridge.popleft()
#     if trucks and weight + trucks[-1] <= l:
#         truck = trucks.pop()
#         weight += truck
#         bridge.append(truck)
#     else:
#         bridge.append(0)
#     time += 1
# print(time)

# 다른사람코드
# weight: 0, now: 0, head: 0, tail: 0, out_time: [-1, -1, -1, -1]
# weight: 7, now: 1, head: 1, tail: 0, out_time: [2, -1, -1, -1]
# weight: 7, now: 2, head: 1, tail: 0, out_time: [2, -1, -1, -1]
# weight: 4, now: 3, head: 2, tail: 1, out_time: [2, 4, -1, -1]
# weight: 9, now: 4, head: 3, tail: 1, out_time: [2, 4, 5, -1]
# weight: 5, now: 5, head: 3, tail: 2, out_time: [2, 4, 5, -1]

N, W, L = map(int, input().split())
lst = list(map(int, input().split()))

weight = 0
now = 0
out_time = [-1] * N
head, tail = 0, 0

while head < N:
    # print(f'weight: {weight}, now: {now}, head: {head}, tail: {tail}, out_time: {out_time}')
    if out_time[tail] == now:
        weight -= lst[tail]
        tail += 1
    if weight + lst[head] <= L:
        out_time[head] = now + W
        weight += lst[head]
        head += 1
    else:
        now = out_time[tail] - 1
    now += 1

print(out_time[-1]+1)