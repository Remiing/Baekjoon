import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M,N,x,y = map(int, input().rstrip().split())
    size = M if M>N else N
    year = x if M>N else y
    while year <= M*N:
        print(year)
        if not (year-x)%M and not (year-y)%N:
            print(year)
            break
        year += size
    else:
        print(-1)

