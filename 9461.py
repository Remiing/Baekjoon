import sys
T = int(sys.stdin.readline().rstrip())
P = [0, 1, 1, 1, 2]
for i in range(4, 100):
    P.append(P[i]+P[i-4])
print(*[P[int(sys.stdin.readline().rstrip())] for x in range(T)], sep='\n')
