# 자리수 이상의 숫자의 개수를 셉니다. 예를들어 n이 120일 때, 자리수가 1이상인 숫자의 개수: 1~120=120개,
# 자리수가 2이상인 숫자의 개수: 10~120=111개, 자리수가 3이상인 숫자의 개수: 100~120=21개 120 + 111 + 21 = 252입니다. 

import sys
input = sys.stdin.readline
n = int(input())
answer = 0
cnt = 1
while n - cnt >= 0:
    answer += n-cnt+1
    cnt *= 10
print(answer)

# 다른사람코드

n = input()
k=0

for i in range(len(n)):
    k+=(int(n)-(10**i)+1)
print(k)
