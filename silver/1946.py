# 서류심사 성적을 a, 면접시험 성적을 b로 두고 a를 내림차순으로 정렬한다.
# a가 1인 사람의 b가 4라고 한다면, a가 1보다 낮은 지원자가 채용되기 위해선 b가 4보다 높아야 한다.
# a가 정렬되어 있는 상태이기 때문에 b만 비교해서 선발된 지원자가 있다면, 그 지원자의 b로 기준을 변경하고 다음 지원자와 비교한다.

import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()
    cnt = 1
    a_score, b_score = score.pop(0)
    for a, b in score:
        if b < b_score:
            cnt += 1
            b_score = b
    print(cnt)

# https://www.acmicpc.net/source/49843246
# 성적에 중복이 없다는 것을 이용해 리스트 대신 딕셔너리를 활용했다.
# 딕셔너리를 활용함으로써 정렬을 할 필요가 없으므로 실행 시간을 줄일 수 있다.

import sys
input = sys.stdin.readline

test = int(input())
pass_lst = []
for _ in range(test):
    n = int(input())
    ranks = [0] * (n + 1)
    for _ in range(n):
        s1, s2 = map(int, input().split())
        ranks[s1] = s2

    cnt = 1
    curr = ranks[1]

    for rank in ranks[2:]:
        if rank < curr:
            cnt += 1
            curr = rank
    pass_lst.append(str(cnt))

print('\n'.join(pass_lst))

