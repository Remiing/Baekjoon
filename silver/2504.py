# string을 한글자씩 읽어서 스택에 쌓으면서, 여는 괄호의 위치를 pointer 리스트에 저장하는 방법을 사용했다.
# replace를 사용하면 더 쉽게 풀 수 있었겠지만 스택을 사용해서 풀고 싶었다. 

import sys
input = sys.stdin.readline
string = input().rstrip()
stack = []
pointer = []
for s in string:
    if s == '(' or s == '[':
        stack.append(s)
        pointer.append(len(stack)-1)
    elif s == ')':
        if not pointer or stack[pointer[-1]] != '(': print(0); exit()
        loc = pointer.pop()
        value = stack[loc+1:]
        if not value:
            value = 1
        else:
            value = sum(value)
        del stack[loc:]
        stack.append(value*2)
    elif s == ']':
        if not pointer or stack[pointer[-1]] != '[': print(0); exit()
        loc = pointer.pop()
        value = stack[loc+1:]
        if not value:
            value = 1
        else:
            value = sum(value)
        del stack[loc:]
        stack.append(value*3)

if pointer:
    print(0)
else:
    print(sum(stack))

# 다른사람코드
# 나는 여는괄화와 닫는괄호 사이를 확인해서 곱하거나 더했지만, 이 코드는 여는괄호가 나오면 임시 변수에 미리 곱해두고 닫는괄호가 나오면 합산하는 방법을 사용했다.
import sys

s=sys.stdin.readline().replace("\n","")
li=[]
total=0
tmp=1
for i in range(len(s)):
    if s[i] == "(":
        li.append(s[i])
        tmp*=2
    elif s[i] == "[":
        li.append(s[i])
        tmp*=3
    elif s[i] == ")":
        if not li or li[-1] == "[":
            total = 0
            break
        elif s[i-1] == "(":
            total+=tmp
        li.pop()
        tmp//=2
    else:
        if not li or li[-1] == "(":
            total=0
            break
        elif s[i-1] == "[":
            total+=tmp
        li.pop()
        tmp//=3

if li:
    print(0)
else:
    print(total)
