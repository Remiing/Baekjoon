# 원리 그대로 코드를 작성하면, 끝자리가 0부터 0까지 끝나는 dp 리스트를 만들어 놓고, 다음 dp는 전항에서 자기보다 같거나 작은 숫자들을 더한다.
# 예를들어 2자리수의 끝자리가 0~9인 수의 개수는 각 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이고, 3자리수의 끝자리가 4인 수의 개수는 1+2+3+4인 10이다.

import sys
input = sys.stdin.readline
n = int(input())
dp = [1]*10
for i in range(1, n):
    num = 0
    for j in range(10):
        num += dp[j]
        dp[j] = num
    print(dp)


print(sum(dp)%10007)

# 다른사람코드
N = int(input())
ans = 1
for i in range(1, 10): ans = ans * (N+i) // i
print(ans % 10007)










