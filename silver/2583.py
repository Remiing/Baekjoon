# dfs를 이용해 풀었다. 
import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
recs = [tuple(map(int, input().split())) for _ in range(k)]
area = [[0]*n for _ in range(m)]
for rec in recs:
    for a in range(rec[1], rec[3]):
        for b in range(rec[0], rec[2]):
            area[a][b] = 1

nums = []
queue = []
for i in range(m):
    for j in range(n):
        if area[i][j]:
            num = 0
            continue
        else:
            queue += [(j, i)]
            area[i][j] = 1
            num = 1
        while queue:
            x, y = queue.pop()
            for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
                if 0 <= nx < n and 0 <= ny < m and not area[ny][nx]:
                    queue += [(nx, ny)]
                    area[ny][nx] = 1
                    num += 1
        nums += [num]

nums = sorted(nums)
print(len(nums))
print(*nums)










