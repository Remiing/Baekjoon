# 3*3 리스트로 주사위를 펼쳤을 때 십자모양을 할당하고, 주사위의 윗부분을 따로 변수로 만들었습니다.
# dice : 명령어가 나올대마다 주사위를 회전시키고 회전시킨 주사위 상태를 리턴합니다.

import sys
input = sys.stdin.readline
n, m, y, x, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

current_dice = [[0]*3 for _ in range(3)]
current_dice_top = 0

def dice(dl, top, cmd):
    if cmd == 1:
        top, dl[1][0], dl[1][1], dl[1][2] = dl[1][0], dl[1][1], dl[1][2], top
    elif cmd == 2:
        top, dl[1][0], dl[1][1], dl[1][2] = dl[1][2], top, dl[1][0], dl[1][1]
    elif cmd == 3:
        top, dl[0][1], dl[1][1], dl[2][1] = dl[2][1], top, dl[0][1], dl[1][1]
    else:
        top, dl[0][1], dl[1][1], dl[2][1] = dl[0][1], dl[1][1], dl[2][1], top
    return dl, top

d = ((1, 0), (0, 1), (0, -1), (-1, 0))
for command in commands:
    dy, dx = d[command % 4][0], d[command % 4][1]
    if not 0 <= y + dy < n or not 0 <= x + dx < m:
        continue
    y, x = y + dy, x + dx
    current_dice, current_dice_top = dice(current_dice, current_dice_top, command)
    print(current_dice_top)
    if not board[y][x]:
        board[y][x] = current_dice[1][1]
    else:
        current_dice[1][1] = board[y][x]
        board[y][x] = 0

# 다른사람코드
# 

N, M, X, Y, K = input_list()
W = [input_list() for _ in range(N)]
D = input_list()

T = 0
B = 0
S = [None, 0, 0, 0, 0]
dX = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]

for d in D:
    if X + dX[d][0] in (-1, N):
        continue
    if Y + dX[d][1] in (-1, M):
        continue
    X, Y = X + dX[d][0], Y + dX[d][1]

    o = d + 1 if d%2 == 1 else d - 1
    T, B, S[d], S[o] = S[o], S[d], T, B
    print(T)

    if W[X][Y] == 0:
        W[X][Y] = B
    else:
        B = W[X][Y]
        W[X][Y] = 0




