# 이전 곡의 가능한 볼륨 리스트 p_list를 가져와서, i번째 곡을 연주할 때 가능한 볼륨을 모두 vol_list에 저장한다. 이후 vol_list을 p_list로 옮기고 vol_list를 비운다.
# 처음 정답 제출할 때 vol_list를 list로 했었는데 메모리 초과가 떠서 중복제거하기 위해 set으로 바꿨고, vol_list를 p_list로 옮기는 동시에 vol_list를 초기화 해서 메모리 초과를 해결했다.

import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

vol_list = set()
p_list = [s]
for i in range(n):
    for p in p_list:
        v1 = p + v[i]
        v2 = p - v[i]
        if 0 <= v1 <= m: vol_list.add(v1)
        if 0 <= v2 <= m: vol_list.add(v2)
    if not vol_list:
        print(-1)
        exit(0)
    p_list, vol_list = list(vol_list), set()
print(max(p_list))

# https://www.acmicpc.net/source/54243382
# 내 코드의 경우 가능한 볼륨을 리스트에 넣었다면, 이분은 최대 볼륨의 수만큼 False로 채워진 리스트를 만들고 가능한 볼륨만 True로 바꾸는 식이다.
# P+V[i]는 M과만 비교하고, P-V[i]는 0과만 비교하는 디테일이 있다.

import sys
input = sys.stdin.readline

n, start, max_v = map(int, input().split())
V = list(map(int, input().split()))
DP = [False]* (max_v + 1)
DP[start] = True

for vol in V:
    new_DP = [False]* (max_v + 1)
    for i in range(len(DP)):
        if DP[i]:
            if i-vol >= 0: new_DP[i-vol] = True
            if i+vol <= max_v: new_DP[i+vol] = True
    DP = new_DP

for i in range(len(DP)-1, -1, -1):
    if DP[i]:
        print(i)
        exit(0)
print(-1)
