# 소수구하기: 에라토스테네스의 체: 숫자들을 배열해 놓고 배수가 되는 수를 지워나가는 방법
# 소수리스트를 만들때 [for j in range(i, len(odd_lst), i)] 이렇게 돌리면 중복확인 하기 때문에 굉장히 오래걸렸다.
# 1000까지의 소수를 구한다고 할 때, for문을 반복하다 i가 17이라면 앞서 (2, 3, 5, 7, 11, 13)의 배수를 지웠기때문에 17*17=289부터 17의 배수를 지우면 된다.
# 지우고나면 289까지 까지 odd_lst값이 True인 i는 확정 소수이다. 따라서 같은 맥락으로 1000까지의 소수를 구하려면 31*31=961, 32*32=1024로 31까지만 확인하면 된다.

import sys
input = sys.stdin.readline
odd_lst = [False]*2 + [True]*(1000000-1)
max_num = len(odd_lst)
for i in range(2, max_num):
    if i*i > max_num: break
    if odd_lst[i]:
        for j in range(i*i, max_num, i):
            odd_lst[j] = False

while True:
    n = int(input())
    if not n: break
    for i in range(3, n//2+1, 2):
        if odd_lst[i] and odd_lst[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")

# 다른사람코드
# sieve 리스트를 슬라이싱해서 한번에 False로 바꾸는 코드가 있는것을 알았다.

import sys

input = sys.stdin.readline
print = sys.stdout.write
max = 1000001

def sol():
    sieve = [False] * 2 + [True] * (max - 2)
    for i in range(3, int(max ** 0.5) + 1):
        if sieve[i]:
            sieve[2 * i::i] = [False] * ((max - i - 1) // i)
    prime = []
    for i in range(3, max, 2):
        if sieve[i]:
            prime.append(i)
    while True:
        n = int(input())
        if n == 0: break

        for i in prime:
            if sieve[n - i]:
                print("%d = %d + %d\n" % (n, i, n - i))
                break

sol()
