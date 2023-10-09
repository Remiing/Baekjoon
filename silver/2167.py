import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = [[0] * (m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m+1):
        array[i][j] += array[i-1][j] + array[i][j-1] - array[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, y, x = map(int, input().split())
    print(array[y][x] - array[y][j-1] - array[i-1][x] + array[i-1][j-1])







