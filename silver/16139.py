import sys
input = sys.stdin.readline
s = input().strip()
dl = [{alp: 0 for alp in 'abcdefghijklmnopqrstuvwxyz'}]
for i in range(len(s)):
    new_dict = dl[-1].copy()
    new_dict[s[i]] += 1
    dl.append(new_dict)
for _ in range(int(input())):
    alp, l, r = input().split()
    print(dl[int(r)+1][alp] - dl[int(l)][alp])









