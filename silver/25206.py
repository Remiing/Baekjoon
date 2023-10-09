import sys
input = sys.stdin.readline
sum1 = 0
sum2 = 0
sdict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    _, a, b = input().split()
    if b == 'P':
        continue
    a = float(a)
    sum1 += sdict[b] * a
    sum2 += a

if not sum2:
    print(0)
else:
    print(sum1/sum2)





