import sys
N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().rstrip().split()))
sort_X = sorted(list(set(X)))
dict_X = {sort_X[i]:i for i in range(len(sort_X))}
print(*[dict_X[i] for i in X])

#index를 활용하면 시간복잡도때문에 시간초과가 된다

import sys
stdin = sys.stdin.buffer

stdin.readline()
arr = list(map(int, stdin.read().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join(map(str, [dic[x] for x in arr])))
