# dp[j]는 그 숫자를 선택했을때 최대값을 가지는 결과이다.
# 예를 들어 수열이 {10, 20, 15, 30, 20, 50}일때 이해하기 쉽도록 dp를 구성한다면
# j=1 dp=[(10), (10, 20), ...]
# j=2 dp=[(10), (10, 20), (10, 15), ...]
# j=3 dp=[(10), (10, 20), (10, 15), (10, 20, 30), ...]
# j=4 dp=[(10), (10, 20), (10, 15), (10, 20, 30), (10, 15, 20), ...]
# j=5 dp=[(10), (10, 20), (10, 15), (10, 20, 30), (10, 15, 20), (10, 20, 30, 50)]

import sys
input = sys.stdin.readline
n = int(input())
num_lst = list(map(int, input().split()))
dp = [1]*n
for j in range(1, n):
    for i in range(0, j):
        if num_lst[i] < num_lst[j]:
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))

# 다른사람코드
# num_lst를 하나씩 보다가 스택의 마지막 값보다 크면 스택에 쌓고 작으면 스택 처음값부터 하나씩 비교하면서 최소값을 갱신한다. 
def sol():
    N = int(input())
    nums = [*map(int,input().split())]
    stack = [nums[0]]

    for i in nums[1:]:
        if stack[-1] < i:
            stack.append(i)
        else:
            for j,v in enumerate(stack):
                if i <= v:
                    stack[j] = i
                    break
    return len(stack)

print(sol())
