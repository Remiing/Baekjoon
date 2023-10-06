# 반시계방향으로 회전하기 때문에 1 다음 3, 2 다음 4, 3 다음 2, 4 다음 1이 나오는 경우는 움푹 들어간 사각형 입니다.

import sys
input = sys.stdin.readline
k = int(input())
w = [tuple(map(int, input().split())) for _ in range(6)]
width, height = 0, 0
small_box = 0
for i in range(6):
    before, after = w[i], w[(i+1) % 6]
    if before[0] == 1:
        if after[0] == 3:
            small_box = before[1] * after[1]
        width = max(width, before[1])
    elif before[0] == 2:
        if after[0] == 4:
            small_box = before[1] * after[1]
        width = max(width, before[1])
    elif before[0] == 3:
        if after[0] == 2:
            small_box = before[1] * after[1]
        height = max(height, before[1])
    else:
        if after[0] == 1:
            small_box = before[1] * after[1]
        height = max(height, before[1])

print((height*width-small_box)*k)

# 다른사람코드
# 입력받은 순서에서 가장 긴 변의 다음다음 혹은 다음다음다음이 움푹 들어간 사각형이라는 것을 이용

n = int(input())
arr = [0,0,0,0,0,0]
for i in range(6) :
    temp, arr[i] = map(int,input().split())
x = arr.index(max(arr))
if arr[(x + 1) % 6] < arr[(x + 5) % 6] :
    y = (x + 5) % 6
    sx = (x + 2) % 6
    sy = (x + 3) % 6
else :
    y = (x + 1) % 6
    sx = (x + 4) % 6
    sy = (x + 3) % 6

print(n * (arr[x] * arr[y] - arr[sx] * arr[sy]))

