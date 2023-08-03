# 처음에 나무를 높이순으로 정렬하고, 높이를 한칸씩 올릴때마다 자른나무에 더해서 목표가 되면 높이를 출력하도록 짰는데 시간초과가 났다.
# 이분탐색으로 처음 풀때 low = mid + 1, high = mid - 1에서 1을 더하거나 빼서 탐색하다 목표를 지나치면 어쩌나 했었는데 직접 돌려보니 그럴 수 없는 알고리즘 이었다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
high, low = max(trees), 0
while high >= low:
    mid = (high + low) // 2
    total = sum([tree-mid if tree-mid > 0 else 0 for tree in trees])
    if total >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)

# 다른사람코드
# 대부분 비슷했다.
