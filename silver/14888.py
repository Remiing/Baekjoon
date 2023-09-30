# 백트래킹을 통해 각 단계마다 값을 계산하고 끝까지 계산했으면 answer 리스트에 결과 값을 넣는다.
# answer 리스트에서 최대값과 최대값을 출력한다.

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
answer = []

def dfs(calc_num, idx):
    if idx == n:
        answer.append(calc_num)
        return
    for oper in [0, 1, 2, 3]:
        if opers[oper]:
            opers[oper] -= 1
            if oper == 0:
                new_calc_num = calc_num + nums[idx]
            elif oper == 1:
                new_calc_num = calc_num - nums[idx]
            elif oper == 2:
                new_calc_num = calc_num * nums[idx]
            else:
                if calc_num < 0:
                    new_calc_num = -(-calc_num // nums[idx])
                else:
                    new_calc_num = calc_num // nums[idx]
            dfs(new_calc_num, idx+1)
            opers[oper] += 1
    return

dfs(nums[0], 1)

print(max(answer))
print(min(answer))

# 다른사람코드
# 나는 opers를 일종의 전역변수로 놓고 함수를 돌렸지만 opers를 함수 인자로 넣어서 계산하면 좀 더 읽기 쉽다.
# 나는 일단 answer에 넣고 최대값과 최소값을 찾았지만 answer에 넣지 않고 최대값과 최소값을 계속 갱신하면 실행시간을 줄일 수 있다.

n = int(input())
arr = list(map(int, input().split()))
cal = list(map(int, input().split()))
maxV = -(10**9)
minV = 10 ** 9

def dfs(prevV, idx, plus, minus, multi, divide):
    global minV, maxV
    if idx == n:
        if minV > prevV:
            minV = prevV
        if maxV < prevV:
            maxV = prevV

    else:
        if plus:
            dfs(prevV + arr[idx], idx + 1, plus - 1, minus, multi, divide)
        if minus:
            dfs(prevV - arr[idx], idx + 1, plus, minus - 1, multi, divide)
        if multi:
            dfs(prevV * arr[idx], idx + 1, plus, minus, multi - 1, divide)
        if divide:
            if prevV < 0:
                dfs(-(abs(prevV) // arr[idx]), idx + 1, plus, minus, multi, divide - 1)
            else:
                dfs(prevV // arr[idx], idx + 1, plus, minus, multi, divide - 1)


dfs(arr[0], 1, *cal)
print(maxV)
print(minV)




