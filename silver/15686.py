from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
house, chicken = [], []
for i in range(n):
    low = list(map(int, input().split()))
    for j in range(n):
        if low[j] == 1:
            house.append((i, j))
        elif low[j] == 2:
            chicken.append((i, j))

chicken_road = [[0] * len(house) for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(house)):
        chicken_road[i][j] = abs(house[j][0] - chicken[i][0]) + abs(house[j][1] - chicken[i][1])

min_total = float('inf')
for com in combinations(chicken_road, m):
    total = 0
    for i in range(len(house)):
        total += min([com[j][i] for j in range(m)])
    min_total = min(min_total, total)
print(min_total)


