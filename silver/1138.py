# 키가 가장 큰 순서(입력받은 순서의 역순)부터 리스트에 넣습니다. for문을 돌며 입력을 받을 때 answer 리스트에는 자신보다 큰 사람들만 있습니다.
# 예를들어, [6 1 1 1 2 0 0]의 경우 맨 처음 (0, 7)을 입력받고 answer에 7을 넣습니다.
# 다음으로 6이 들어갈 수 있는 곳은 7의 앞(0) 혹은 뒤(1) 입니다. (0, 6)을 입력받았기 때문에 answer[0]에 6을 넣습니다.
# 다음으로 5가 들어갈 수 있는 곳은 6의 앞(0) 혹은 6과 7 사이(1) 혹은 7 뒤(2) 입니다. (2, 5)를 입력받았기 때문에 자신보다 큰 숫자가 2개란 뜻이고, answer 가장 맨 뒤에 5를 넣습니다.

import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))

answer = []
for num, height_seq in list(enumerate(seq, start=1))[::-1]:
    answer.insert(height_seq, num)
print(*answer)

# 다른사람코드
# 

N=int(input())
h=list(map(int,input().split()))[::-1]
o=[]
for i in h:
    o.insert(i,N)
    N-=1
print(*o)

