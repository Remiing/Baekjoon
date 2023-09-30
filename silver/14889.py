# 단순하게 모든 조합을 구해서 최소값을 구했다. 시간이 굉장히 오래걸림

from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
total = set(range(n))

for com in combinations(range(n), n//2):
    t1 = set(com)
    t2 = total - t1
    t1_score = sum([s[c1][c2] + s[c2][c1] for c1, c2 in combinations(t1, 2)])
    t2_score = sum([s[c1][c2] + s[c2][c1] for c1, c2 in combinations(t2, 2)])
    answer = min(answer, abs(t1_score-t2_score))

print(answer)

# 다른사람코드
# [0,1,2,3]의 사람이 있을 때, 0이 들어가는 모든 경우, 1이 들어가는 경우...n이 들어가는 경우를 계산해둔다. (stat_per_member)
# combinations를 사용해서 팀을 만든 뒤 팀의 점수를 계산하고, 모두 한팀이 될 떄의 점수에서 값을 빼는 것으로 차이를 구한다. 

input = sys.stdin.readline


def init():
    totalnum = int(input())
    stat_graph = [list(map(int, input().split())) for _ in range(totalnum)]

    return [totalnum, stat_graph]


def run():
    totalnum, stat_graph = init()
    rows_sum = [sum(row) for row in stat_graph]
    cols_sum = [sum(col) for col in zip(*stat_graph)]  # zip(*graph): graph의 각 열
    stat_per_member = [i + j for i, j in zip(rows_sum, cols_sum)]
    total_stat = sum(rows_sum)

    min_score = total_stat
    for stat in combinations(stat_per_member, totalnum // 2):
        val = abs(total_stat - sum(stat))
        if val < min_score:
            min_score = val
    print(min_score)

run()
