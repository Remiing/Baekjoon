# 입력받은 배열의 맨 앞과 맨 뒤 인덱스를 옮기는 방법을 사용합니다.
# idx[0]은 배열의 맨 앞, idx[1]은 배열의 맨 뒤 입니다.
# R을 입력받으면 reverse 변수를 통해 뒤집어진 상태를 저장하고, D 명령어가 나왔을 때 앞의 인덱스를 늘릴지, 뒤의 인덱스를 줄일지 정합니다.

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    p = input().rstrip().replace('RR', '')
    n = int(input())
    nums = input().rstrip()[1:-1].split(',')
    idx = [0, n-1]
    reverse = False
    for pp in p:
        if pp == 'R':
            reverse = not reverse
        elif idx[0] <= idx[1] and pp == 'D':
            if reverse:
                idx[1] -= 1
            else:
                idx[0] += 1
        else:
            print('error')
            break
    else:
        if reverse:
            nums = [nums[i] for i in range(idx[1], idx[0]-1, -1)]
        else:
            nums = [nums[i] for i in range(idx[0], idx[1]+1)]
        print('['+','.join(nums)+']')

# 다른사람코드
# RR이 붙어 나오는 경우를 없앤뒤, R을 기준으로 명령어를 나눕니다. 그렇게되면 짝수번째 인덱스의 명령어는 앞에서부터, 홀수번째 인덱스의 명령어는 뒤에서부터 잘라내게 됩니다.

def Sol():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        commands = [*map(len, input().rstrip().replace("RR", "").split("R"))]
        is_flip = (len(commands) + 1) % 2

        n = int(input())
        if n == 0:
            input()
            arr = []
        else:
            arr = input().strip("[]\n").split(",")

        front = sum(commands[0::2])
        try:
            back = sum(commands[1::2])
        except:
            back = 0


        if front + back > n:
            print("error")
            continue
        else:
            arr = arr[front:(n-back)]

        print(f'[{",".join(reversed(arr) if is_flip else arr)}]')


if __name__ == "__main__":
    Sol()





