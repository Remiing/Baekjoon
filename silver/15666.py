import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = sorted(list(set(map(int, input().split()))))

def bt(current, sub):
    if len(current) == m:
        print(*current)
        return
    for i in range(len(sub)):
        new_current = current[:]
        new_current.append(sub[i])
        bt(new_current, sub[i:])
    return

bt([], array)

