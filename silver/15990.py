# dp의 각 인덱스에 [1로끝나는경우, 2로끝나는경우, 3으로끝나는경우]를 저장해서 입력받은 숫자의 최대값까지 구합니다.

import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
max_num = max(nums)
dp = [[0, 0, 0] for _ in range(max_num+1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, max_num+1):
    dp[i] = [(dp[i-1][1] + dp[i-1][2]) % 1000000009, (dp[i-2][0] + dp[i-2][2]) % 1000000009, (dp[i-3][0] + dp[i-3][1]) % 1000000009]
for num in nums:
    print(sum(dp[num]) % 1000000009)

# 다른사람코드
# dp를 3개로 나눠 d1엔 1로 끝나는 경우, d2엔 2로 끝나는 경우, d3엔 3으로 끝나는 경우를 저장하고 입력받은 숫자의 최대값까지 값을 구합니다.

l = [int(input()) for _ in range(int(input()))]
m = max(l)
div = 1000000009
d1 = [1, 0, 1]
d2 = [0, 1, 1]
d3 = [0, 0, 1]
for i in range(4, m+1):
    d1.append((d2[-1] + d3[-1]) % div)
    d2.append((d1[-3] + d3[-2]) % div)
    d3.append((d1[-4] + d2[-4]) % div)
for x in l:
    print((d1[x-1] + d2[x-1] + d3[x-1]) % div)
