import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
site = {}
for _ in range(N):
    key, value = map(str, sys.stdin.readline().rstrip().split())
    site[key] = value
q = [sys.stdin.readline().rstrip() for _ in range(M)]
print(*[site[x] for x in q], sep='\n')

