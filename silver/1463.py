import sys
N = int(sys.stdin.readline().rstrip())
dp = [0, 0]
for i in range(2, N+1):
    min_value = dp[i-1]
    if i%3==0:
        min_value = min(min_value, dp[i//3])
    if i%2==0:
        min_value = min(min_value, dp[i//2])
    dp.append(min_value + 1)
print(dp[N])
