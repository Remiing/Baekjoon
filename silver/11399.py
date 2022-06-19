import sys
N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))
P.sort(reverse = True)
S=0
for i in range(len(P)):
    S += P[i]*(i+1)
print(S)
