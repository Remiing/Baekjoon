import sys
input = sys.stdin.readline
n = int(input())
nums = [0]*8002
sum_num = 0
min_num, max_num, mid_num = False, False, False
most_num, most, same = 0, 0, False

for _ in range(n):
    num = int(input())
    sum_num += num
    nums[num+4001] += 1
mid_cnt = n // 2 + 1
for i in range(1, len(nums)):
    if nums[i]:
        if not min_num:
            min_num = i
        max_num = i
        mid_cnt -= nums[i]
        if mid_cnt <= 0 and not mid_num:
            mid_num = i
        if nums[i] > most:
            most = nums[i]
            most_num = i
            same = False
        elif nums[i] == most and not same:
            most_num = i
            same = True
print(f'{round(sum_num/n)}\n{mid_num - 4001}\n{most_num - 4001}\n{max_num - min_num}')







