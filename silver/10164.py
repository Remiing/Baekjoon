# y*x 크기의 dp 리스트를 만들고 모든 칸을 돌면서 경우의 수를 계산합니다.
# (1,1)부터 o의 위치인 (oy,ox)까지의 경우의 수와 (oy,ox)부터 (y,x)까지의 경우의 수를 곱해서 출력합니다. 

import sys
input = sys.stdin.readline
y, x, o = map(int, input().split())
o = 1 if not o else o
oy, ox = (o-1) // x, (o-1) % x
dp = [[1]*x for _ in range(y)]
for i in range(1, y):
    for j in range(1, x):
        if (i <= oy and j <= ox) or (i > oy and j > ox):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[oy][ox] * dp[y-1][x-1])

# 다른사람코드
# 최단거리의 경우의 수를 계산하는 방법은 조합으로 생각할 수 있습니다.
# 예를 들어 (1,1)에서 (3,5)까지 이동한다고 하면 오른쪽으로 5번, 아래로 3번 이동해야 합니다.
# 그리고 경로의 개수는 오른쪽 5번, 아래 3번의 조합으로 생각할 수 있습니다.
# 따라서 n개 중에서 같은 것이 p개, q개 있을 때 조합의 수를 계산하는 식은 (n!)/(p!q!), (8!)/(5!3!) = (40320)/(120*6) = 40320/720 = 56입니다.

def combination(n, r):
    num, rest = 1, 1

    for i in range(r):
        num *= n - i
        rest *= i + 1

    return num // rest


n, m, k = map(int, input().split())
if k == 0:
    print(combination(n + m - 2, min(n, m) - 1))
else:
    k -= 1
    p, q = k // m, k % m
    a, b = n - p - 1, m - q - 1

    print(combination(p + q, min(p, q)) * combination(a + b, min(a, b)))

