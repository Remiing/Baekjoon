# 블루레이의 크기를 이분탐색으로 찾도록 했습니다.
# 예를들어 start가 0, end가 10이라면 mid는 5입니다. 블루레이 크기가 5일때 블루레이의 개수를 세고 start, end를 조정합니다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
class_list = list(map(int, input().split()))
start, end = max(class_list), 1000000000
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    bs = 0
    for i in range(n):
        if bs + class_list[i] <= mid:
            bs += class_list[i]
        else:
            cnt += 1
            bs = class_list[i]
    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)

