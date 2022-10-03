import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()

i=0
part = 0
count = 0
while i<M-2:
    if S[i:i+3] == 'IOI':
        part += 1
        i += 2
        if part == N:
            count += 1
            part -= 1
    else:
        part = 0
        i += 1
print(count)


# else code
i=input
n=int(i());i();
print(sum(max(0,len(s)-n)for s in i().replace('IO','X').replace('XI','XXO').replace('I','O').split('O')))
