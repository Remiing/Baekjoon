import sys
input = sys.stdin.readline

an, am = map(int, input().split())
amatrix = [tuple(map(int, input().split())) for _ in range(an)]

bn, bm = map(int, input().split())
bmatrix = [tuple(map(int, input().split())) for _ in range(bn)]
bmatrix = tuple(zip(*bmatrix))

answer = [[0]*bm for _ in range(an)]
for i in range(an):
    for j in range(bm):
        answer[i][j] = sum([a * b for a, b in zip(amatrix[i], bmatrix[j])])

for row in answer:
    print(*row)





