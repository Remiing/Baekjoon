# i번째 숫자가 들어오면 0 ~ i-1 까지 숫자 중에서 자신보다 작은 숫자에 자신을 더한 숫자 중 최대값을 dp에 저장합니다.
# total_array = [1, 100, 2, 50, 60,  3, 5,  6,  7,  8]
#          dp = [1, 101, 3, 53, 113, 6, 11, 17, 24, 32]

import sys
input = sys.stdin.readline
n = int(input())
total_array = list(map(int, input().split()))
dp = [0]*n
print(total_array)
for i in range(n):
    dp[i] = max([dp[j] + total_array[i] for j in range(i) if total_array[j] < total_array[i]] + [total_array[i]])
print(dp)
print(max(dp))

# 다른사람코드
# dp를 구성하는 방법이 조금 다르다. 각 dp에는 그 숫자로 끝나는 값 중 최대값을 저장합니다.
# 예를들어 위의 예제에서 입력이 60이 들어왔을때 dp[1]=1, dp[100]=101, dp[2]=3, dp[50]=53, 그 외의 dp는 0입니다.
# 따라서 dp[1]부터 dp[59] 중에서 최대값인 dp[50]에 60을 더해 dp[60]에 저장합니다. 

input()
dp = [0] * 1001
for i in map(int, input().split()):
    dp[i] = max(dp[:i]) + i

print(max(dp))





