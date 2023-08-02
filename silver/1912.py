# dp[i]에는 num_lst[i]의 값과 dp[i-1]+num_lst[i]의 값 중 큰값을 저장한다. 

import sys
input = sys.stdin.readline
n = int(input())
num_lst = list(map(int, input().split()))
dp = [num_lst.pop(0)] + [0]*(n-1)
for i, n in enumerate(num_lst, start=1):
    dp[i] = max(n, dp[i-1]+n)
print(max(dp))

# 다른사람코드
# 사실 이 코드가 구현하고 싶었던 코드였는데 정리가 안돼서 dp로 풀었었다.
# m=최대값, p=임시로 더한값을 저장
def main() -> None:
    _, *A = map(int, os.read(0, os.fstat(0).st_size).split())

    m = -0x3F3F3F3F
    p = -1

    for a in A:
        if p <= 0:
            p = 0
        p += a
        if p > m:
            m = p

    print(m)








