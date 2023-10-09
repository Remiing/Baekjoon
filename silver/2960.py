import sys
input = sys.stdin.readline
n, m = map(int, input().split())
prime = [True] * (n+1)
for i in range(2, len(prime)):
    if prime[i]:
        for j in range(i, len(prime), i):
            if prime[j]:
                prime[j] = False
                m -= 1
            if not m:
                print(j)
                exit()







