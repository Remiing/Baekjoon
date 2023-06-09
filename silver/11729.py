# n개의 원판이 start에 쌓여있는 상태에서 시작하면 n-1개의 원판을 가운데 sub 장대에 쌓고 start에 남은 가장 큰 원판을 end로 옮긴후 sub에 있는 n-1개의 원판을 end로 옮긴다.
# 전체적인 흐름은 위와 같고 n > n-1 > n-2 > ... > 1개의 원판까지 반복한다.

import sys
input = sys.stdin.readline
n = int(input())

def hanoi(n, start, sub, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, end, sub)
    print(start, end)
    hanoi(n-1, sub, start, end)
    return

print(2**n - 1)
hanoi(n, 1, 2, 3)