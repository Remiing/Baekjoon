import sys
T = int(sys.stdin.readline().rstrip())
n_list = list(map(int, [sys.stdin.readline().rstrip() for _ in range(T)]))
sum_list = [0, 1, 2, 4]
for i in range(4, 12):
    sum_list.append(sum(sum_list[i-3:i]))
print(*[sum_list[x] for x in n_list], sep='\n')
