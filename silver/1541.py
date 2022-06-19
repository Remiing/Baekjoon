import sys
polynomial = list(sys.stdin.readline().rstrip().split('-'))
for i in range(len(polynomial)):
    polynomial[i] = -sum(map(int,polynomial[i].split('+')))
polynomial[0] = -polynomial[0]
print(sum(polynomial))

