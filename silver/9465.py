# 맨 처음에 dp1과 dp2로 나누지 않고 각 단계별 최대값을 담은 하나의 dp 리스트로 하려했지만 조건을 맞출 수 없었다.
# 1행 dp1과 2행 dp2로 나누어 한칸 대각으로 합치는 경우, 두칸 대각으로 합치는 경우로 나눌 수 있다.

import sys
input = sys.stdin.readline

def sticker(s1, s2):
    dp1 = [s1[0]] + [s2[0]+s1[1]] + [0]*(n-2)
    dp2 = [s2[0]] + [s1[0]+s2[1]] + [0]*(n-2)

    for i in range(2, n):
        dp1[i] = max(dp2[i-1], dp2[i-2]) + s1[i]
        dp2[i] = max(dp1[i-1], dp1[i-2]) + s2[i]

    return max(dp1[-1], dp2[-1])

t = int(input())
for _ in range(t):
    n = int(input())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    if n==1: print(max(s1[0], s2[0]))
    else: print(sticker(s1, s2))

# 다른사람코드
# 나는 dp리스트를 따로 만들었지만 1행 up, 2행 down이라는 변수만으로 문제를 해결헀다.
def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = [None, None]
        arr[0] = list(map(int, input().split()))
        arr[1] = list(map(int, input().split()))

        up = 0
        down = 0

        for i in range(n):
            up, down = max(down + arr[0][i], up), max(up + arr[1][i], down)

        print(max(up, down))
        