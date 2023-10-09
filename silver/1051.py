import sys
input = sys.stdin.readline
n, m = map(int, input().split())
box = [list(input().rstrip()) for _ in range(n)]
side = min(n, m)
for d in range(side-1, -1, -1):
    for y in range(n-d):
        for x in range(m-d):
            if box[y][x] == box[y+d][x] == box[y][x+d] == box[y+d][x+d]:
                print((d+1)**2)
                exit()







