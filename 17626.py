import sys
import time
a=time.time()
n = int(sys.stdin.readline().rstrip())
min_list = [0, 1]
for i in range(2, n+1):
    j=1
    min_list.append(min([min_list[i-j**2] for j in range(1, int(i**(0.5))+1)]) + 1)
print(min_list[n])
print(time.time()-a)
