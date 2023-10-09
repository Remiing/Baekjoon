import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

d = ((-1, 0), (0, -1), (1, 0), (0, 1))
def find():
    visited = [[False] * n for _ in range(n)]
    open_list = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                sum_popular = country[i][j]
                visited[i][j] = True
                q = [(i, j)]
                open = [(i, j)]
                while q:
                    y, x = q.pop()
                    for dy, dx in d:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and l <= abs(country[y][x] - country[ny][nx]) <= r:
                            sum_popular += country[ny][nx]
                            q.append((ny, nx))
                            visited[ny][nx] = True
                            open.append((ny, nx))
                if len(open) > 1:
                    open_list.append((sum_popular//len(open), open))
    return open_list

cnt = 0
while country_list := find():
    for area in country_list:
        new_popular, countries = area
        for cy, cx in countries:
            country[cy][cx] = new_popular
    cnt += 1

print(cnt)




