# nCm에서 0의 개수 즉, 소인수분해 했을 떄 2와 5의 개수를 구하는 문제입니다.
# 예를 들어 n=25, m=12일 때, 2의 개수는 (25~14에서 2의 배수의 개수)-(12~1에서 2의 배수의 개수)=(25까지의 2의 배수의 개수)-(13까지의 2의 배수의 개수)-(12까지의 2의 배수의 개수)입니다.
# 단 2의 배수, 4의 배수, 8의 배수 등등을 모두 더해야 합니다.
# 마찬가지로 5의 개수도 센 뒤 둘 중 작은 값을 출력합니다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
m = min(n-m, m)
n2, n5 = 0, 0

k = 1
while k * 2 <= n:
    k *= 2
    n2 -= m//k
    n2 += (n//k) - ((n-m)//k)

k = 1
while k * 5 <= n:
    k *= 5
    n5 -= m//k
    n5 += (n//k) - ((n-m)//k)

print(min(n2, n5))

# 다른사람코드
#

def ffiff(n,k):
    cnt=0
    while n>0:
        n//=k
        cnt+=n
    return cnt

n,m=map(int,input().split())

n2=ffiff(n,2)-(ffiff(n-m,2)+ffiff(m,2))
n5=ffiff(n,5)-(ffiff(n-m,5)+ffiff(m,5))

print(min(n2,n5))
