# 이항계수의 식 n!/((n-k)!k!)을 이용했습니다.

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num = 1
for i in range(n, k, -1):
    num *= i
for i in range(n-k, 1, -1):
    num //= i
print(num % 10007)

# 다른사람코드
# 예를들어 n=8, k=3일때, 답은 8!/(5!3!) = (8*7*6)/(3*2*1)입니다. 따라서 UP=8*7*6, DOWN=1*2*3으로 만들고 나누어 답을 출력합니다. 

N,K=map(int,input().split())
UP=1
DOWN=1
for i in range(K):
    UP*=(N-i)
    DOWN*=(i+1)
print((UP//DOWN)%10007)




