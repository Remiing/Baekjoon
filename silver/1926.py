import sys
input = sys.stdin.readline
n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]
max_area = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if painting[i][j]:
            cnt += 1
            queue = [(i, j)]
            painting[i][j] = 0
            painting_area = 1
            while queue:
                y, x = queue.pop(0)
                for ny, nx in [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]:
                    if 0 <= ny < n and 0 <= nx < m and painting[ny][nx]:
                        queue.append((ny, nx))
                        painting[ny][nx] = 0
                        painting_area += 1
            max_area = max(max_area, painting_area)
print(cnt)
print(max_area)







