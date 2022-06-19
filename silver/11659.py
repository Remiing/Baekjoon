import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
num_list.insert(0, 0)
for i in range(1, N+1):
    num_list[i] += num_list[i-1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(num_list[j] - num_list[i-1])
