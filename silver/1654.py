# 백준 2805 이분탐색과 같은 유형인데, 그 문제와는 마지막 line_max를 선택하는 방법이 좀 달라서 어렵다.

import sys
input = sys.stdin.readline
k, n = map(int, input().split())
line_lst = [int(input()) for _ in range(k)]
short, long = 1, max(line_lst)
line_max = 0
while short <= long:
    mid = (short+long)//2
    line_num = sum(line//mid for line in line_lst)
    if line_num >= n:
        line_max = mid
        short = mid + 1
    else:
        long = mid -1
print(line_max)

# 다른사람코드
# 나는 중간에 line_max = mid를 통해 조건이 맞을때의 값을 저장해뒀는데 long값을 리턴해도 답이 되는 것 같다. 
from sys import stdin

input = stdin.readline

k, n = map(int, input().rstrip().split())
l = [int(input()) for _ in range(k)]
M = sum(l) // n
m = 1

while m <= M:
  mid = (m + M) // 2
  if sum([i // mid for i in l]) >= n:
    m = mid + 1
  else:
    M = mid - 1
print(M)
