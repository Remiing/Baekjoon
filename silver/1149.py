# rgb 각 색을 선택했을 때의 최솟값을 각각 저장해두고 다음 집을 선택할 때 새로 최솟값을 갱신한다

import sys
input = sys.stdin.readline
n = int(input())

cost = [list(map(int, input().split())) for _ in range(n)]
total_cost = [0, 0, 0]
for r, g, b, in cost:
    total_cost = [r+min(total_cost[1], total_cost[2]), g+min(total_cost[0], total_cost[2]), b+min(total_cost[0], total_cost[1])]

print(min(total_cost))


