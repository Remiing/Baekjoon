# 0으로 끝나는 경우를 모두 탐색해서 최소값을 찾습니다. 

from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
cost_list = [list(map(int, input().split())) for _ in range(n)]
answer = []
for per in permutations(range(1, n), n-1):
    per = list(per)
    per.append(0)
    sum_cost = 0
    for i in range(n):
        if cost := cost_list[per[i]][per[(i+1) % n]]:
            sum_cost += cost
        else:
            break
    else:
        answer.append(sum_cost)
print(min(answer))

# 다른사람코드
#

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]


def find(visited, now):
    if (visited << N) | now in dp:
        return dp[(visited << N) | now]
    if visited == (1 << N) - 1:
        return cost[now][0] if cost[now][0] > 0 else 10 ** 9

    tmp = 10 ** 8
    for i in range(1, N):
        if not visited & (1 << i) and cost[now][i]:
            tmp = min(tmp, find(visited | (1 << i), i) + cost[now][i])

    dp[visited << N | now] = tmp
    return tmp

dp = {}

print(find(1, 0))






