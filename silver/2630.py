import sys
arr = []
count = [0, 0]
N = int(sys.stdin.readline())

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

def func(x, y, N):
    if N == 1:
        count[arr[x][y]] += 1
    else:
        for i in range(N):
            for j in range(N):
                if arr[x][y] != arr[x+i][y+j]:
                    for a in range(x, x+N, N//2):
                        for b in range(y, y+N, N//2):
                            func(a, b, N//2)
                    return None
        count[arr[x][y]] += 1
        return None

func(0, 0, N)

print(count[0])
print(count[1])
