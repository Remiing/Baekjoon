# t : 톱니바퀴 리스트, tti : 각 톱니바퀴의 가장 위에 있는 기어 인덱스

import sys
input = sys.stdin.readline
t = [[]] + [input().rstrip() for _ in range(4)]
tti = [0, 0, 0, 0, 0]
k = int(input())
for _ in range(k):
    temp = [0, 0, 0, 0, 0]
    tn, d = map(int, input().split())
    temp[tn] = d
    ti = tn
    while 0 < ti - 1 and t[ti][(tti[ti]-2) % 8] != t[ti-1][(tti[ti - 1]+2) % 8]:
        temp[ti - 1] = temp[ti] * (-1)
        ti -= 1
    ti = tn
    while ti + 1 <= 4 and t[ti][(tti[ti] + 2) % 8] != t[ti+1][(tti[ti + 1] - 2) % 8]:
        temp[ti + 1] = temp[ti] * (-1)
        ti += 1
    for i in range(1, 5):
        tti[i] = (tti[i] + temp[i] * (-1)) % 8

score = 0
for i in range(1, 5):
    if t[i][tti[i]] == '1':
        score += 2**(i-1)
print(score)