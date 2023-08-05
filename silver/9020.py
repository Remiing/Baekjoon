# 다른 소수 구하는 문제와 다를 것 없지만 n이 4일때의 예외와 6, 10, 14와 같이 2로 나눈 수가 홀수 일때의 경우를 나눠야 한다.

import sys
input = sys.stdin.readline
t = int(input())

prime_number = [False]*2 + [True]*(10000-1)
for i in range(3, 101, 2):
    if prime_number[i]:
        prime_number[i*i::i*2] = [False]*len(prime_number[i*i::i*2])
for _ in range(t):
    n = int(input())
    if n//2 % 2:
        start = n//2
    else:
        start = n//2 - 1
    for i in range(start, 2, -2):
        if prime_number[i] and prime_number[n-i]:
            print(i, n-i)
            break
    else:
        print(2, 2)

