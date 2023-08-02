# 먼가 스택 push pop으로 풀면 오래 걸릴 것 같아서 다른 방법을 풀었는데 오히려 더 오래걸린 것 같다.
import sys
input = sys.stdin.readline
n = int(input())
num_lst = [0] + [int(input()) for _ in range(n)]
stack = [1]*(n+1)
sign = ''
for i in range(1, n+1):
    before, after = num_lst[i-1], num_lst[i]
    if before < after:
        sign += '+'*sum(stack[before+1:after+1])
    else:
        if sum(stack[after:before+1]) != 1:
            print('NO')
            exit()
    sign += '-'
    stack[after] = 0

print(*sign, sep='\n')

# 다른사람코드

def solution():
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    s = []
    answer = []
    cur = 1
    for value in nums:
        while cur <= value:
            answer.append('+')
            s.append(cur)
            cur += 1
        if s.pop() != value:
            return "NO"
        answer.append('-')
    return '\n'.join(answer)


print(solution())





