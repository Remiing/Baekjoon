# dp[0]에는 마지막 칸에 사자를 안넣는 경우, dp[1]에는 오른쪽에 사자를 넣는 경우와 왼쪽에 사자를 넣는 경우를 합친 값을 넣었다.
import sys
input = sys.stdin.readline
n = int(input())
dp = [1, 2]    # 00, 01+10
for i in range(1, n):
    dp[0], dp[1] = sum(dp), dp[0]*2+dp[1]

print(sum(dp)%9901)

# 다른사람코드
# 나같은 경우에 00과 01,10으로 나누었는데 이분은 합쳐놓고 전항을 이용했다.
# (A+B)% p = [(A% p) + (B% p)] % p 나머지 분배법칙을 이용해 미리 9901로 나눠둔다.  
n = int(input())
a, b = 1, 3
for _ in range(n):
    a, b = b, (a + 2 * b) % 9901
print(a)












