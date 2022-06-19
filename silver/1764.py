import sys
N,M = map(int, sys.stdin.readline().rstrip().split())
a = set([sys.stdin.readline().rstrip() for _ in range(N)])
b = set([sys.stdin.readline().rstrip() for _ in range(M)])
ab = sorted(list(a & b))
print(len(ab))
print(*ab, sep = '\n')
