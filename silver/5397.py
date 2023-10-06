import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    test = list(input().rstrip())
    left = []
    right = []
    for t in test:
        if t == '<':
            if left:
                right.append(left.pop())
        elif t == '>':
            if right:
                left.append(right.pop())
        elif t == '-':
            if left:
                left.pop()
        else:
            left.append(t)
    print(''.join(left + right[::-1]))









