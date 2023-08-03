# 0~n*2 크기의 리스트에서 소수는 1, 아닌것은 0으로 만들고 범위가 주어지면 범위 내의 값들을 모두 더해서 답을 구한다. 
import sys
input = sys.stdin.readline
max_num = 123456*2
prime_number = [0]*2 + [1]*(max_num-1)
for i in range(2, int(max_num**0.5+1)):
    if prime_number[i]:
        prime_number[i*i::i] = [0]*(max_num//i-(i-1))
while True:
    n = int(input())
    if not n: break
    print(sum(prime_number[n+1:2*n+1]))

# 다른사람코드
# 소수를 구할때 슬라이싱에 2*i를 해서 2의 배수는 배제한채로 구한다.
# 소수를 구할때 prime_number 리스트를 0, 1로 하지 않고, True, False로 함으로써 크기를 줄였고, True인 i값만 모아서 리스트를 새로 만든다.
# 그후에 이분탐색을 통해 주어진 숫자 범위 내에서 최대값 소수의 인덱스와 최소값 소수의 인덱스를 빼서 답을 구한다.
def prime(n):
    if n <= 1:
        return []
    sieve = [True] * (n + 1)
    for i in range(3, int(n ** .5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * len(sieve[i * i::2 * i])
    return [2] + [i for i in range(3, n + 1, 2) if sieve[i]]

def Search(prime, n):
    l, r = 0, len(prime) - 1
    while l <= r:
        m = (l + r) // 2

        if prime[m] > n:
            r = m - 1
        else:
            l = m + 1
    return l

primeList = prime(123456 * 2)
while True:
    input = int(sys.stdin.readline().strip())
    if input != 0:
        print(Search(primeList, input * 2) - Search(primeList, input))
    else:
        break
