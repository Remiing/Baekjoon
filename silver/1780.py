import sys
N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
count = [0, 0, 0]
def cutting(side_len, a, b):
    side = []
    for i in range(side_len):
        side += matrix[a+i][b:b+side_len]
    side = list(set(side))
    if len(side) != 1:
        for i in range(3):
            for j in range(3):
                cutting(side_len//3, a+side_len//3*i, b+side_len//3*j)
    else:
        count[side[0]+1]+=1

cutting(N, 0, 0)
print(count[0])
print(count[1])
print(count[2])


#else code
import sys

arr = []
count = [0, 0, 0]

n = int(sys.stdin.readline())

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

def func(x, y, N):
    if N == 1:
        count[arr[x][y]+1] += 1
        return None

    else:
        for i in range(N):
            for j in range(N):
                if arr[x+i][y+j] != arr[x][y]:
                    for a in range(x, x + N, N // 3):
                        for b in range(y, y + N, N // 3):
                            func(a, b, N // 3)

                    return None

        count[arr[x][y]+1] += 1
        return None

func(0, 0, n)

print(count[0])
print(count[1])
print(count[2])
