import sys
input = sys.stdin.readline
string = input().rstrip()
nd = {}
for s in string:
    if nd.get(s):
        nd[s] += 1
    else:
        nd[s] = 1

nd = sorted(nd.items())
answer = ''
center = ''

if len(string) % 2 == 0:
    for s, cnt in sorted(nd):
        if cnt % 2 == 1:
            print("I'm Sorry Hansoo")
            exit()
        answer += s*(cnt//2)
else:
    for s, cnt in sorted(nd):
        if cnt % 2 == 1 and center:
            print("I'm Sorry Hansoo")
            exit()
        elif cnt % 2 == 1:
            center = s
            cnt -= 1
        answer += s*(cnt//2)

answer = answer + center + answer[::-1]
print(answer)

# 다른사람코드
#

inp = input().rstrip()
dict = {}
for alpha in inp:
    dict.setdefault(alpha, 0)
    dict[alpha] += 1

ans, center = '', ''
for alpha, cnt in sorted(dict.items()):
    if cnt%2:
        if center != '':
            print("I'm Sorry Hansoo")
            break
        center = alpha
    ans += alpha * (cnt//2)
else:
    print(ans + center + ans[::-1])


