import sys
input = sys.stdin.readline
sn = int(input())
switch = [0] + list(map(int, input().split()))

n = int(input())
for _ in range(n):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(num, sn+1, num):
            switch[i] = (switch[i] + 1) % 2
    else:

        for i in range(min(num - 1, sn-num) + 1):
            left = num - i
            right = num + i
            if switch[left] != switch[right]:
                break
            switch[left] = switch[right] = (switch[right] + 1) % 2

for i in range(1, sn+1, 20):
    print(*switch[i:i+20])



