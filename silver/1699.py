# 백트래킹도 써보고, 여러 방법을 다 써봤는데 이 방법이 가장 빨랐다.
# dp[i]를 i보다 작은 제곱수들로 뺀 값들 중에서 가장 작은 값에 1을 더해 갱신하는 방법입니다.
# 예를들어 dp[43]은 dp[43-36], dp[43-25], dp[43-16], dp[43-9], dp[43-4], dp[43-1]중 최소값을 찾아 1을 더하고 저장합니다.

import sys
input = sys.stdin.readline
n = int(input())
dp = [1]*2 + [100000]*(n-1)
for i in range(2, n+1):
    min_square = i**0.5
    if int(min_square) == min_square:
        dp[i] = 1
    else:
        dp[i] = min([dp[i-j*j] for j in range(1, int(min_square) + 1)]) + 1

print(dp[-1])

# 다른사람코드
# 답이 1, 2, 3, 4인 경우를 나눠서 풀었다.

def solve(n):
    if n == 0: return 0
    if n == int(n ** 0.5) ** 2: return 1

    while n % 4 == 0 and n > 0: n //= 4
    if n % 8 == 7: return 4

    for i in range(1, int((n / 2) ** 0.5) + 1):
        if i ** 2 + int((n - i ** 2) ** 0.5) ** 2 == n:
            return 2

    return 3


print(solve(int(input())))
