# 단순히 a**b%c 계산식으로 계산하면 시간초과가 된다.
# 모듈로 거듭제곱법 A^B mod C = ((A mod C)^B) mod C, 모듈로 곱셈 (A * B) mod C = (A mod C * B mod C) mod C 수식과 재귀함수를 통해 정답을 구한다.

import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())

def mod(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return mod(a * a % c, b // 2, c)
    else:
        return a * mod(a, b - 1, c) % c

print(mod(a, b, c))
