# 그냥 재귀 돌렸다가 n이 커지면 시간초과가 됩니다.
# 우선 옮기는 개수는 2**n-1입니다.
# 1층일때 옮기는 횟수는 1, 2층일때는 1층일때의 경우*2+1 = 3, 3층일때는 2층일때의 경우*2+1 = 7 > 2**n-1

import sys
input = sys.stdin.readline
n = int(input())
def hanoi(a, b, c, num):
    if num == 1:
        print(a, c)
        return
    hanoi(a, c, b, num-1)
    print(a, c)
    hanoi(b, a, c, num-1)
    return

print(2**n-1)
if n <= 20:
    hanoi(1, 2, 3, n)
