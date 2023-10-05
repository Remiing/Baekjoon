# 원본 리스트를 정렬해서 가장 큰값을 q에 두고 array에서 맨 앞과 맨 뒤 값 중 q에 넣었을 때 차가 최대가 되는 값을 q에 추가합니다.

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
array = deque(sorted(list(map(int, input().split()))))
q = deque([array.pop()])
answer = 0
while array:
    a1, a2 = abs(q[0]-array[0]), abs(q[-1]-array[0])
    b1, b2 = abs(q[0]-array[-1]), abs(q[-1]-array[-1])
    max_value = max(a1, a2, b1, b2)
    if a1 == max_value:
        answer += a1
        q.appendleft(array.popleft())
    elif a2 == max_value:
        answer += a2
        q.append(array.popleft())
    elif b1 == max_value:
        answer += b1
        q.appendleft(array.pop())
    elif b2 == max_value:
        answer += b2
        q.append(array.pop())
print(answer)

# 다른사람코드
#

import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
A.sort()
mini = A[0]
maxi = A[-1]
sum = maxi - mini
A = A[1:-1]
while len(A) > 0:
    if len(A) != 1:
        a = A[0]
        b = A[-1]
        sum += maxi - a
        sum += b - mini
        maxi = b
        mini = a
        A = A[1:-1]
    else:
        a = A[0]
        sum += max(maxi-a, a-mini)
        break
print(sum)