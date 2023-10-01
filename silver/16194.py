# for j in range((i-1)//2+1): p[i] = min(p[i], p[j]+p[i-1-j]) 처럼 매 for문마다 min을 계산하는 것보다
# p[i] = min([p[i]] + [p[j] + p[i - 1 - j] for j in range((i-1)//2+1)]) 처럼 값을 모두 구해놓고 min을 찾는 것이 훨씬 빠르다.

import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))

for i in range(n):
    p[i] = min([p[i]] + [p[j] + p[i - 1 - j] for j in range((i-1)//2+1)])
print(p[n-1])
