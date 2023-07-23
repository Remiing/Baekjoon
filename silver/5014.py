# 맨 처음에 dfs로 풀었다가 오답이 나와서 최단거리를 풀 때 dfs를 쓰면 안된다는 것을 알았다.
# dfs는 시작점에서 도착점까지 가는 모든 경로를 탐색해봐야 하지만, bfs는 목적지에 도착한 순간이 최단경로이기 때문이다.

import sys
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())   # F=건물층수, S=현재층, G=목적지층, U=위로가는단위수, D=아래로가는단위수
building = [-1]*(f+1)
building[s] = 0
queue = [s]
while queue:
    current = queue.pop(0)
    for i in [current+u, current-d]:
        if 1<=i<=f and building[i] == -1:
            building[i] = building[current] + 1
            queue += [i]
num = building[g]
if num != -1: print(num)
else: print('use the stairs')

# 다른사람코드
# 

f, s, g, u, d = map(int, sys.stdin.readline().split())
if s == g: print(0); exit()
elif s > g and s > d > 0:
    r = (s-g)//d
    s -= r*d
elif s < g and s+u <= f and u > 0:
    r = (g-s)//u
    s += r*u
elif s > g and d <= 0 or s < g and u <= 0: print('use the stairs'); exit()
else: r = 0
while r<f and 0<s<=f:
    if s==g:print(r);exit()
    s+=-d if s>g and s>d or s<g and s+u>f else u
    r+=1
print('use the stairs')









