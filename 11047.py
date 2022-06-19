import sys
N,K = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
num = 0
for i in reversed(coins):
    num += K//i
    K = K%i
print(num)
