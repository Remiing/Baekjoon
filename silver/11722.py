import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
q = [array[0]]
for i in range(1, n):
    if q[-1] > array[i]:
        q.append(array[i])
    else:
        for j in range(len(q)):
            if q[j] <= array[i]:
                q[j] = array[i]
                break
print(len(q))

