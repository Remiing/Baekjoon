import sys
T = int(sys.stdin.readline().rstrip())
N = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
fibo_list = [[1,0], [0,1]]
for i in range(2,41):
    fibo_list.append([x+y for x,y in zip(fibo_list[i-1], fibo_list[i-2])])
for i in N:
    print(*fibo_list[i])
