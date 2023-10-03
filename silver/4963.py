import sys
input = sys.stdin.readline

def dfs(ml):
    w, h = len(ml[0]), len(ml)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if ml[i][j]:
                q = [(i, j)]
                ml[i][j] = 0
                while q:
                    y, x = q.pop()
                    for ny, nx in [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x+1), (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1)]:
                        if 0 <= ny < h and 0 <= nx < w and ml[ny][nx]:
                            q.append((ny, nx))
                            ml[ny][nx] = 0
                cnt += 1
    return cnt


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    ml = [list(map(int, input().split())) for _ in range(h)]
    print(dfs(ml))

