# 처음에 k개 만큼 딕셔너리에 추가합니다. 이후 0부터 n까지 돌면서 i번째 초밥을 딕셔너리에서 빼고, i+k번째 초밥을 새로 추가한뒤 초밥 종류의 최대값을 갱신합니다. 

import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(n)]
kind_dict = {c: 1}
kind_num = 0
for i in range(k):
    in_dish = dishes[i]
    if in_dish not in kind_dict:
        kind_dict[in_dish] = 0
    kind_dict[in_dish] += 1

for i in range(n):
    in_dish = dishes[(i + k) % n]
    out_dish = dishes[i]
    if in_dish not in kind_dict:
        kind_dict[in_dish] = 0
    kind_dict[in_dish] += 1
    if kind_dict[out_dish] == 1:
        del kind_dict[out_dish]
    else:
        kind_dict[out_dish] -= 1
    if len(kind_dict) > kind_num:
        kind_num = len(kind_dict)
        if kind_num == k+1:
            break
print(kind_num)

# 다른사람코드
# 굳이 딕셔너리를 사용해서 초밥의 개수를 세지 않고, 새로운 초밥이 들어올 때와 나갈 때 종류의 개수를 늘리거나 줄입니다.

def initResult():
    res = 0

    for num in nums[:k]:
        if cache[num] == 0:
            res += 1
        cache[num] += 1

    return res


def slide():
    ans = initResult()
    cnt = ans

    for i in range(0, n):
        if ans <= cnt:
            ans = cnt if cache[c] else cnt + 1

        left = nums[i]
        right = nums[(i + k) % n]

        cache[left] -= 1

        if cache[left] == 0: cnt -= 1
        if cache[right] == 0: cnt += 1

        cache[right] += 1

    return ans


nums = []
n, d, k, c = map(int, input().split())
for _ in range(n):
    nums.append(int(input()))

cache = [0] * (d + 1)

print(slide())




