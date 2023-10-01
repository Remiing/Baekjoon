# matrix1, matrix2의 왼쪽 위부터 한칸씩 비교하면서 다르면 3x3 뒤집기 연산을 합니다.
# 끝까지 연산을 한 뒤 두 행렬이 다르면 -1, 같으면 뒤집기 연산을 한 횟수를 출력합니다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix1 = [list(input().rstrip()) for _ in range(n)]
matrix2 = [list(input().rstrip()) for _ in range(n)]
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if matrix1[i][j] != matrix2[i][j]:
            for a in range(3):
                for b in range(3):
                    if matrix1[i+a][j+b] == '1':
                        matrix1[i+a][j+b] = '0'
                    else:
                        matrix1[i+a][j+b] = '1'
            cnt += 1
if matrix1 != matrix2:
    answer = -1
else:
    answer = cnt

print(answer)
