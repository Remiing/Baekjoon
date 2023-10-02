# 연속된 빈 좌석에서의 개수는 피보나치 수열로 셀 수 있습니다. 예를 들어, 1칸이 비면 1, 2칸이 비면 2, 3칸이 비면 3, 4칸이 비면 5, 5칸이 비면 8...
# 입력을 받을 때마다 연속된 빈 좌석을 계산해서 답을 출력합니다.

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

dp = [1, 1, 2] + [0]*38
for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

answer, i = 1, 0
for _ in range(m):
    j = int(input())
    answer *= dp[j - i - 1]
    i = j

print(answer*dp[n-i])

# 다른사람코드
# 마지막 값을 계산하기 위해 나는 print(answer*dp[n-i])처럼 작업을 한번 더 따로 했지만, vip 좌석에 (n+1) 좌석이 있다고 생각하면 따로 계산을 안해도 됐었다. 

N = int(input())
M = int(input())
vip_seat = [int(input()) for _ in range(M)] + [N+1]

fibo = [1,1]
for _ in range(N):
    fibo.append(fibo[-1]+fibo[-2])

answer = 1
temp = 1
for i in vip_seat:
    answer *= fibo[i - temp]
    temp = i + 1
print(answer)





