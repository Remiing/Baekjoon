# 이분탐색을 이용해서 예산을 찾습니다.

import sys
input = sys.stdin.readline
n = int(input())
budget_list = list(map(int, input().split()))
m = int(input())
start, end = 0, max(budget_list)
while start <= end:
    mid = (start + end) // 2
    total = sum([budget if budget < mid else mid for budget in budget_list])
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# 다른사람코드
# 각 지방의 예산을 오름차순으로 정렬합니다. 이후 첫 번째 지방의 예산부터 돌면서 예산을 정합니다.
# 예를들어 n=5, budget=[120, 110, 140, 150], m=485일 때, 가장 적은 예산은 110이고 485/4=121.2입니다. 즉 첫 번째 지방이 필요한 예산을 전부 주어도 다른 지방의 예산엔 영향을 미치지 않습니다. 따라서 전체 예산에서 110을 빼줍니다.
# 다음으로 큰 지방의 예산은 120입니다. 375/3=125로 마찬가지로 이후 나올 지방의 예산에 영향을 미치지 않습니다.
# 다음으로 큰 지방의 예산은 140입니다. 255/2=127입니다. 이 경우 남은 예산을 남은 지방끼리 똑같이 나누어야 합니다.

N = int(sys.stdin.readline().rstrip())
budget = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

budget.sort()
for i in range(N):
    if ((M / (N - i)) <= budget[i]):
        answer = M // (N - i)
        break

    answer = budget[i]
    M -= budget[i]
print(answer)


