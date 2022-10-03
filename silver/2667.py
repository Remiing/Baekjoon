import sys
input = sys.stdin.readline
N = int(input())
map = [list(map(int, input().rstrip())) for _ in range(N)]

block_count = 0
house_count = []

for r, row in enumerate(map):
    for c, num in enumerate(row):
        if num:
            count = 1
            map[r][c] = 0
            stack = [(r,c)]
            while stack:
                x,y = stack.pop()
                for nx, ny in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
                    if 0<=nx<N and 0<=ny<N and map[nx][ny]:
                        stack.append((nx,ny))
                        map[nx][ny] = 0
                        count+=1
            block_count += 1
            house_count.append(count)

print(block_count)
print(*sorted(house_count), sep='\n')
