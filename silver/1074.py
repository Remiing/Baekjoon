import sys
N, r, c = map(int, sys.stdin.readline().rstrip().split())
count = 0
while N>0:
    half = 2**(N-1)
    i = 0
    if c>=half:
        i += 1
        c -= half
    if r>=half:
        i += 2
        r -= half
    count += 4**(N-1)*i
    N -= 1
print(count)
