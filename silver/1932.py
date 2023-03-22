# 삼각형 맨 윗줄부터 차례로 돌면서 각 숫자마다 대각선 왼쪽 혹은 대각선 오른쪽 중 큰것을 자신과 더한다.

import sys

input = sys.stdin.readline
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: triangle[i][j] += triangle[i-1][0]
        elif j == i: triangle[i][j] += triangle[i-1][-1]
        else: triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))

# acmicpc.net/source/53892726
# 내 코드는 전체 삼각형을 입력받은 후 한줄씩 돌면서 결과 값을 구했지만
# 이 코드는 nums라는 리스트에 한줄씩 입력을 받으면서, prev에 최대값이 담긴 리스트를 생성한다.
# 이런 방식이면 메모리 낭비를 막을 수 있다.

import sys
input = sys.stdin.readline

N = int(input())
prev = [*map(int, input().split())]

for i in range(1, N):
  nums = [*map(int, input().split())]
  b = [max(prev[j-1], prev[j])+nums[j] for j in range(1, i)]
  prev = [prev[0]+nums[0], *b, prev[-1]+nums[-1]]

print(max(prev))
