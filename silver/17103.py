import sys
input = sys.stdin.readline
n = int(input())
test_case = [int(input()) for _ in range(n)]
mn = max(test_case)
prime = [True] * (mn + 1)
for i in range(2, len(prime)):
    if prime[i]:
        prime[i**2::i] = [False] * len(prime[i**2::i])
for even_num in test_case:
    cnt = 0
    for i in range(2, even_num//2+1):
        if prime[i] and prime[even_num-i]:
            cnt += 1
    print(cnt)

# 다른사람코드

def make_eratos():
    eratos = [False,False,True] + [True,False]*499999
    for i in range(3,1001,2):
        if eratos[i]:
            eratos[2*i::i] = [False]*(1000000//i-1)
    prime = [i for i,x in enumerate(eratos) if x]
    return eratos, prime

def cnt_gbpart(N):
    cnt = 0
    for x in prime:
        tmp = N - x
        if x > tmp:
            break
        else:
            if eratos[tmp]:
                cnt += 1
    return cnt

from sys import stdin
input = stdin.readline

eratos, prime = make_eratos()
n = int(input())

for _ in range(n):
    N = int(input())
    print(cnt_gbpart(N))






