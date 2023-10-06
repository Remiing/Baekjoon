# land_list에 0~256까지 그 층수에 해당하는 칸이 몇개 있는지 저장합니다.
# land_list의 가장 높은 곳과 낮은 곳을 비교합니다.
# 만약 인벤토리의 블록이 가장 낮은 블록의 수보다 적거나, 가장 높은 곳의 블록을 한 칸씩 내리는 것보다 가장 낮은 곳의 블록을 한 칸씩 올리는 게 싼 경우 가장 높은 칸을 한 칸씩 내립니다.

import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
land = sum([list(map(int, input().split())) for _ in range(n)], [])
land_list = [0]*257
time = 0
low, high = 0, 256
for l in land:
    land_list[l] += 1
while low < high:
    if not land_list[low]:
        low += 1
        continue
    if not land_list[high]:
        high -= 1
        continue
    if b < land_list[low] or land_list[low] > land_list[high] * 2:
        b += land_list[high]
        time += 2*land_list[high]
        land_list[high-1] += land_list[high]
        high -= 1
    else:
        b -= land_list[low]
        time += land_list[low]
        land_list[low+1] += land_list[low]
        low += 1

print(time, high)

# 다른사람코드
# have=총블럭개수, 1층부터 올라가면서 그 층을 만드는 데 필요한 시간을 계산해서 최소값을 만듭니다. 

def sol():
    n, m, b = map(int, input().split())
    data = [0]*257
    for _ in range(n):
        for i in map(int, input().split()):
            data[i] += 1
    have = sum(i*data[i] for i in range(257))
    ans = (have*2, 0)
    need = 0
    t = data[0]
    nm = n*m
    for i in range(1, 257):
        need += t
        have -= nm-t
        t += data[i]
        if have+b-need < 0:
            break
        else:
            ans = min((have*2+need, -i), ans)
    print(ans[0], -ans[1])
sol()
