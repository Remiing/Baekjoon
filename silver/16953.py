# q에 2*n, 10*n+1과 연산횟수를 넣고 bfs를 활용해서 풀었습니다.

from collections import deque
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
q = deque([(a, 1)])
while q:
    n, cnt = q.popleft()
    for nn in (n*2, n*10+1):
        if nn < b:
            q.append((nn, cnt+1))
        elif nn == b:
            print(cnt + 1)
            exit()
print(-1)

# 다른사람코드
# 나는 a를 b에 맞추는 방법을 선택헀지만, b를 a로 만드는 방법읩니다.
# 만약 b를 a로 만드는 연산이 성립되지 않으면 중단하기 때문에 실행시간이 줄어듭니다. 

A,B=map(int, input().split())
count=1

while A<B:
    if B%2==0:
        B=B//2
    elif B%10 ==1:
        B=B//10
    else:
        break
    count+=1

if A==B:
    print(count)
else:
    print(-1)




