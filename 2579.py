import sys
N = int(sys.stdin.readline().rstrip())
stairs = list(map(int, [sys.stdin.readline().rstrip() for _ in range(N)]))
stairs.insert(0, 0)
if N==1:
    print(stairs[1])
else:
    dp=[0]
    dp.append(stairs[1])
    dp.append(stairs[1]+stairs[2])
    for i in range(3, N+1):
        dp.append(max(dp[i-2], dp[i-3]+stairs[i-1])+stairs[i])
    print(dp[-1])
