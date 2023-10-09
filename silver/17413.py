import sys
input = sys.stdin.readline
s = input().rstrip()
stack = []
check = False
for i in range(len(s)):
    if s[i] == '<':
        while stack:
            print(stack.pop(), end='')
        check = True
        print(s[i], end='')
    elif s[i] == '>':
        check = False
        print(s[i], end='')
    elif s[i] == ' ':
        while stack:
            print(stack.pop(), end='')
        print(s[i], end='')
    else:
        if check:
            print(s[i], end='')
        else:
            stack.append(s[i])

while stack:
    print(stack.pop(), end='')

# 다른사람코드
# 

def sol(seq: str) -> str:
    seq: list = seq.replace('>', '<').split('<')
    ans: str = ''

    for i in range(len(seq)):
        if i % 2 == 1:
            ans += f'<{seq[i]}>'
        else:
            ans += reverse_words(seq[i])
    return ans


def reverse_words(words: str) -> str:
    return ' '.join(word[::-1] for word in words.split())


print(sol(stdin.readline().rstrip()))
