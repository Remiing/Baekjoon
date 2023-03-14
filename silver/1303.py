import sys
input = sys.stdin.readline
n, m = map(int, input().split())
field = [list(input().rstrip()) for _ in range(m)]

def dfs(i, j, team):
    cnt = 1
    queue = [(i, j)]
    while queue:
        x, y = queue.pop()
        field[x][y] = 0
        for x, y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0<=x<m and 0<=y<n and field[x][y]==team:
                queue.append((x, y))
                field[x][y] = 0
                cnt += 1
    return cnt * cnt

w, b = 0, 0
for x in range(m):
    for y in range(n):
        if field[x][y] == 'W':
            w += dfs(x, y, 'W')
        elif field[x][y] == 'B':
            b += dfs(x, y, 'B')
print(w, b)

