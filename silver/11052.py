# (1장짜리 카드팩 + N-1개의 카드를 구하는 최대값), (2장짜리 카드팩 + N-2개의 카드를 구하는 최대값), ... (N-1장짜리 카드팩 + 1개의 카드를 구하는 최대값), (N장짜리 카드팩)
# 위의 값 중 제일 큰 값을 dp[n]에 넣는다.

import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    dp[i] = max([p[j]+dp[i-j-1] for j in range(i)])

print(dp[-1])

