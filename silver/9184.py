# 문제 조건에 맞게 재귀를 만들고, 그대로 제출하면 같은 a,b,c를 여러번 계산하기 때문에 dp에 값을 저장해뒀다가 리턴합니다.

import sys
input = sys.stdin.readline
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        a, b, c = 0, 0, 0
    if a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]

while True:
    n1, n2, n3 = map(int, input().split())
    if n1 == n2 == n3 == -1:
        break
    print(f'w({n1}, {n2}, {n3}) = {w(n1, n2, n3)}')
