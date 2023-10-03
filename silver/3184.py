# 단순하게 garden을 순회하면서 #이 아니면 큐에 넣고 dfs를 돌려서 영역 내의 양과 늑대의 개수를 셉니다.
# 영역 내에서 양이 늑대보다 많으면 총 양의 수에 영역 내의 양의 수를 더합니다. 반대일 경우 늑대의 수에 더합니다.

import sys
input = sys.stdin.readline
r, c = map(int, input().split())
garden = [list(input().rstrip()) for _ in range(r)]
sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if garden[i][j] != '#':
            sheep_cnt, wolf_cnt = 0, 0
            if garden[i][j] == 'o':
                sheep_cnt = 1
            elif garden[i][j] == 'v':
                wolf_cnt = 1
            garden[i][j] = '#'
            q = [(i, j)]
            while q:
                y, x = q.pop()
                for ny, nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
                    if 0 <= ny < r and 0 <= nx < c and garden[ny][nx] != '#':
                        if garden[ny][nx] == 'o':
                            sheep_cnt += 1
                        elif garden[ny][nx] == 'v':
                            wolf_cnt += 1
                        garden[ny][nx] = '#'
                        q.append((ny, nx))
            if sheep_cnt > wolf_cnt:
                sheep += sheep_cnt
            else:
                wolf += wolf_cnt

print(sheep, wolf)

# 코드 수정본
# 맨 처음 #이 아니면 큐에 넣었는데 이런식으로 하면 울타리 외부의 공백도 dfs를 하기 때문에 오래걸립니다. 따라서 o나 v일때 dfs를 돌립니다.
# 양이나 늑대는 항상 울타리 내부에 존재하기 때문에 0 <= ny < r and 0 <= nx < c 조건이 필요없다.

r, c = map(int, input().split())
garden = [list(input().rstrip()) for _ in range(r)]
sheep, wolf = 0, 0
for i in range(r):
    for j in range(c):
        if garden[i][j] == 'o' or garden[i][j] == 'v':
            sheep_cnt, wolf_cnt = 0, 0
            if garden[i][j] == 'o':
                sheep_cnt = 1
            elif garden[i][j] == 'v':
                wolf_cnt = 1
            garden[i][j] = '#'
            q = [(i, j)]
            while q:
                y, x = q.pop()
                for ny, nx in [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]:
                    if garden[ny][nx] != '#':
                        if garden[ny][nx] == 'o':
                            sheep_cnt += 1
                        elif garden[ny][nx] == 'v':
                            wolf_cnt += 1
                        garden[ny][nx] = '#'
                        q.append((ny, nx))
            if sheep_cnt > wolf_cnt:
                sheep += sheep_cnt
            else:
                wolf += wolf_cnt

print(sheep, wolf)








