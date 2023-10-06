import sys
input = sys.stdin.readline
n = int(input())
test_case = [int(input()) for _ in range(n)]
dp = [0, 1, 2, 4] + [0]*(max(test_case)-3)
for i in range(4, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
for test in test_case:
    print(dp[test])

