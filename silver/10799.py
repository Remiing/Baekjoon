import sys
input = sys.stdin.readline
lazer = input().rstrip()
cnt = 0
pipe = 0
for i in range(len(lazer)-1):
    if lazer[i:i+2] == '((':
        pipe += 1
        cnt += 1
    elif lazer[i:i+2] == '()':
        cnt += pipe
    elif lazer[i:i+2] == '))':
        pipe -= 1
cnt += pipe
print(cnt)

# 다른사람코드

def solution(parentheses):
    stack = []
    cutting_count = 0

    for ele in parentheses:
        if ele == '(':
            stack.append(ele)
            last = ele
        else:
            if last == '(':
                stack.pop()
                cutting_count += len(stack)
                last = ele
            else:
                stack.pop()
                cutting_count += 1
    return cutting_count


if __name__ == "__main__":
    parentheses = input()
    print(solution(parentheses))

