from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
nums = deque(range(1, n+1))
while nums and len(nums) > 1:
    print(nums.popleft(), end=' ')
    nums.append(nums.popleft())
print(nums[0])







# 1 3 5 7 9 4 8 6 2