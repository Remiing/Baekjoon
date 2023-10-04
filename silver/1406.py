# 처음에 단순하게 커서의 위치 i와 insert, del로 풀었다가 시간초과가 났습니다.
# 커서의 위치 왼쪽의 left_str과 오른쪽의 right_str을 만들고 명령에 따라 append와 pop으로 처리했습니다.
# right_str은 뒤집힌 상태이기 때문에 역순으로 출력해야 합니다. 

import sys
input = sys.stdin.readline
left_str = list(input().rstrip())
right_str = []
n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'L' and left_str:
        right_str.append(left_str.pop())
    elif cmd[0] == 'D' and right_str:
        left_str.append(right_str.pop())
    elif cmd[0] == 'B' and left_str:
        left_str.pop()
    elif cmd[0] == 'P':
        left_str.append(cmd[1])
print(''.join(left_str + right_str[::-1]))








