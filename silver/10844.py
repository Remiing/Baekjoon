# n자리의 숫자들 중 계단수가 몇 개인지 구하는 문제다.
# 각 숫자에서 끝자리 수만 보면서 dp를 구한다.
# 예를 들어, xxxx4처럼 5자리의 끝이 4인 계단수의 개수는 4자리의 끝이 3과 5인 숫자의 합이다.
# 추가로 n자리의 끝이 0인 계단수는 n-1자리의 끝이 1인 계단수만 될 수 있고, n자리의 끝이 9인 계단수는 n-1자리의 끝이 8인 계단수만 될 수 있다.

import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for _ in range(n-1)]
dp.insert(0, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][1]
        elif j == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[-1]) % 1000000000)

# 다른 사람 코드
# 청므에 이해하기 좀 어려웠는데 간단하게 좌우대칭이라는 점을 이용했다.
# 끝자리수 0~9를 a~j로 치환하고 a,b,c,d,e / f,g,h,i,j로 나눠 a+j,b+i,c+h,d+g,e+f로 묶는다.
# 다음 항은 b,a+c,b+d,c+e,d+f / e+g,f+h,g+i,h+j,i이고, 묶으면 b+i,a+c+h+j,b+d+g+i,c+e+f+h,d+f+e+g이다.
# 위의 결과에서 a+j,b+i,c+h,d+g,e+f를 v,w,x,y,z로 치환하면 첫째항 v,w,x,y,z 둘째항 w,v+x,w+y,x+z,y+z가 된다.

a = 1
b = c = d = e = 2

for _ in [0]*(n-1):
    a, b, c, d, e = b, a+c, b+d, c+e, d+e

print((a+b+c+d+e) % 10**9)


