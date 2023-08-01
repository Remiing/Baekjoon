# 최대값 구할때는 부등호의 리스트 왼쪽부터 차례대로 읽으면서 '>'기호가 나오면 정답 문자열에 9~0까지 되돌아가면서 숫자를 넣는다.
# 예를 들어 부등호 리스트가 '< < < > < < > < >'일때 처음 '>' 위치는 i=3이다. 따라서 정답 문자열은 '6789'가 된다.
# 다음 '>'의 위치는 i=6이기때문에 정답 문자열은 '6789345'가 된다. 끝까지 반복하고 부등호 리스트가 끝나면 남은 숫자를 넣는다.
# 최소값을 구할때는 0~9까지 '<'기호가 나오면 숫자를 넣는다.

import sys
input = sys.stdin.readline
k = int(input())
sign = input().split()
max_num = list(range(9, 9-(k+1), -1))
min_num = list(range(0, k+1))
max_ans = [-1]*(k+1)
min_ans = [-1]*(k+1)
for i in range(k+1):
    if i == k or sign[i] == '>':
        j = i
        while j >= 0 and max_ans[j] == -1:
            max_ans[j] = max_num.pop(0)
            j -= 1
    if i == k or sign[i] == '<':
        j = i
        while j >= 0 and min_ans[j] == -1:
            min_ans[j] = min_num.pop(0)
            j -= 1

print(*max_ans, sep='')
print(*min_ans, sep='')

# 다른사람코드
# 
N = input_single()
O = input_list(str)

minS = ''
maxS = ''

minL = maxL = 1
minA, maxB = 0, 9

for o in O:
    if o == ">":
        maxS += "".join(map(str, range(maxB-maxL+1, maxB+1)))
        maxB -= maxL
        maxL = 1
        minL += 1

    elif o == "<":
        minS += "".join(map(str, range(minA+minL-1, minA-1, -1)))
        minA += minL
        minL = 1
        maxL += 1

maxS += "".join(map(str, range(maxB-maxL+1, maxB+1)))
minS += "".join(map(str, range(minA+minL-1, minA-1, -1)))

print(maxS)
print(minS)







