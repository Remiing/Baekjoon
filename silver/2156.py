import sys
input = sys.stdin.readline
n = int(input())
wine_list = [int(input()) for _ in range(n)]
wine_list.insert(0, 0)

dp = [0]*(n+1)
dp[1] = wine_list[1]
if n > 1:
    dp[2] = wine_list[1] + wine_list[2]
for i in range(3, n+1):
    dp[i] = max(wine_list[i] + wine_list[i-1] + dp[i-3], wine_list[i] + dp[i-2], dp[i-1])
print(dp[-1])



