# 최대값까지 리스트를 만들고 소수인 값만 1로 설정합니다.
# 리스트를 n부터 1씩 올리면서 소수라면 팰린드롬 여부를 확인하고 출력합니다.

import sys
input = sys.stdin.readline
n = int(input())
nums = [False]*2 + [True]*1003000
for i in range(len(nums)):
    if nums[i]:
        nums[i*i::i] = [False] * len(nums[i*i::i])
for i in range(n, len(nums)):
    if nums[i]:
        ns = str(i)
        if ns == ns[::-1]:
            print(i)
            break

# 다른사람코드
# 팰린드롬을 찾고 소수판별을 할까, 소수를 찾고 팰린드롬을 확인할까 고민하다 후자를 택했는데, 전자가 더 빠른경우였다.

n = int(input())

def Prime(x):
    for i in range(2,int(x*(0.5))+1):
        if x % i == 0:
            return False
    return True
result = 0
for i in range(n,100001):
    if i == 1:
        continue
    string = str(i)
    rev = string[::-1]
    if string == rev:
        if Prime(i) == True:
            result = i
            break
if result == 0:
    result = 1003001
print(result)
