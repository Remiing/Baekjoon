# for문에서 k를 그 노드를 거치는 경로라고 이해하고 진행해야한다.
# 예를들어, k가 5이라면 1>5>2, 1>5>3, 1>5>4와 같이 k를 거쳐가면서 모든 쌍을 순회하며 경로의 존재 여부를 갱신한다.

import sys
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

for i in matrix:
    print(*i)

