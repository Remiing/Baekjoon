# 맨처음 문제를 봤을때 무지성 for, sum으로 할려다가 M이 100,000개인것을 보고 누적합을 이용해 풀어야한다는 것을 알았다.
# 다만 x축에서만 누적합을 이용해서 풀었다가 시간초과가 떠서 x,y를 합쳐서 다시 풀었다.
# 예를들어, 4x4사이즈의 테이블을 만들때, 마지막 (4,4) table을 채울때는 table[4][3]+table[3][4]를 해주고 (1,1)부터 (3,3)까지 두번 더해졌기 때문에 table[3][3]을 빼주고 (4,4) 값을 더해준다.
# (2,2)에서 (3,4)까지의 합을 구하려면, (1,1)~(3,4)의 합인 table[3][4]에서 (1,1)~(3,1)의 합인 table[3][1]과 (1,1)~(1,4)의 합인 table[1][4]을 빼주고 (1,1)~(1,1)이 두번 빼졌기 때문에 table[1][1]을 더해준다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
table = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    for j in range(1, n+1):
        table[i][j] = table[i][j-1] + table[i-1][j] - table[i-1][j-1] + lst[j-1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    num = table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1]
    print(num)

# 다른사람코드
# x축 누적합을 먼저하고 그 table을 바탕으로 y축 누적합을 했다.
# 실행시간이 좀 더 빨라진다.
def readline():
    return sys.stdin.readline().rstrip()

def main():
    n, m = map(int, readline().split())
    matrix = [[0] * (n + 1)] + [[0] + list(map(int, readline().split()))
                                for _ in range(n)]
    for row in matrix:
        for i in range(n):
            row[i + 1] += row[i]
    for i in range(n):
        upper = matrix[i]
        lower = matrix[i + 1]
        for j in range(n + 1):
            lower[j] += upper[j]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, readline().split())
        print(
            matrix[x2][y2]
            - matrix[x1 - 1][y2]
            - matrix[x2][y1 - 1]
            + matrix[x1 - 1][y1 - 1]
        )
