import sys
input = sys.stdin.readline
n = int(input())
map_list = [list(map(int, input().split())) for _ in range(n)]

def safe_area(h):
    safe_num = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            queue = []
            if map_list[i][j] > h and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = 1
                safe_num += 1
            while queue:
                y, x = queue.pop()
                for ny, nx in [(y-1, x), (y, x-1), (y+1, x), (y, x+1)]:
                    if 0 <= ny < n and 0 <= nx < n and map_list[ny][nx] > h and not visited[ny][nx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = 1
    return safe_num

max_num = 1
max_height = max(map(max, map_list))
for i in range(1, max_height):
    num = safe_area(i)
    max_num = max(max_num, num)

print(max_num)