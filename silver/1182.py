# 백트래킹으로 모든 경우를 탐색하면서 합한 숫자가 s일 때 cnt를 1씩 추가했습니다.

import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(snum, visited, idx):
    global cnt
    for i in range(idx, n):
        if not visited[i]:
            snum += nums[i]
            visited[i] = True
            if snum == s:
                cnt += 1
            dfs(snum, visited, i+1)
            snum -= nums[i]
            visited[i] = False

cnt = 0
visited = [False]*n
dfs(0, visited, 0)
print(cnt)

# 다른사람코드
# 나는 visited 리스트를 두고 일일이 방문했는지 확인하고, idx를 이용해서 어디서부터 숫자를 더할지 정해줬는데, idx만 추가하거나 슬라이싱을 통해 어떤 값을 확인해야 하는지 인자로 넘겨도 됐을 것 같다.
# 시간을 단축하기 위해 수열을 반으로 나누고 각각 백트래킹을 진행해 딕셔너리를 만든 뒤 조합을 계산했습니다. 

import sys
N, S = map(int, sys.stdin.readline().split())

L = list(map(int, sys.stdin.readline().split()))

L_DICT = dict()
R_DICT = dict()

mid = len(L) // 2


def BackTrack(subseq, l, sum_p, index, target_dict):
    if sum_p in target_dict.keys():
        target_dict[sum_p] += 1
    else:
        target_dict[sum_p] = 1

    for i in range(index, len(l)):
        next_l = subseq + [l[i]]
        next_sum = sum_p + l[i]
        BackTrack(next_l, l, next_sum, i + 1, target_dict)
        next_l.pop()


BackTrack([], L[:mid], 0, 0, L_DICT)
BackTrack([], L[mid:], 0, 0, R_DICT)
c = 0
for lp in L_DICT.keys():
    if S - lp in R_DICT.keys():
        c += L_DICT[lp] * R_DICT[S - lp]

if S == 0:
    print(c - 1)
else:
    print(c)



