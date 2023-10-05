# permutations를 이용해서 순열을 짤 수 있지만 백트래킹을 써서 풀어봤다. 

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
answer = set()

def dfs(part, sub):
    if len(part) == m:
        answer.add(tuple(part))
        return
    for i in range(len(sub)):
        new_part = part + [sub[i]]
        dfs(new_part, sub[:i] + sub[i+1:])
    return

dfs([], array)
for a in sorted(list(answer)):
    print(*a)

# 다른사람코드
# dict.fromkeys를 이용하면 순서를 유지하면서 중복을 제거할 수 있다.

_, M, *arr = stdin.read().split()
arr.sort(key=int)
stdout.write('\n'.join(map(' '.join, dict.fromkeys(permutations(arr, int(M))))))




