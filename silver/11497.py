# 만약 통나무가 [1,2,3,4,5,6]으로 있다고 한다면 [5,3,1,2,4,6]으로 재배열해서 각 통나무 사이의 최소값을 출력해줍니다.

import sys
input = sys.stdin.readline
n = int(input())

def calc(array):
    array.sort()
    array = array[::2][::-1] + array[1::2]
    dif_max = abs(array[0] - array[-1])
    for i in range(len(array)-1):
        dif = abs(array[i+1] - array[i])
        if dif > dif_max:
            dif_max = dif
    return dif_max

for _ in range(n):
    _ = input()
    log_list = list(map(int, input().split()))
    print(calc(log_list))

# 다른사람코드
# 나같은경우 모든 경우를 확인했지만 단지 0, 2, 4..번째 인덱스끼리만 확인해도 된다.

for _ in range(int(input())):
    N = int(input())
    Lis = sorted(list(map(int, input().split())))
    print(max([Lis[i+2]-Lis[i] for i in range(N-2)]))
