# bfs와 딕셔너리를 활용해서 풀었다. bfs의 특성상 이미 dp에 값이 있다면 새롭게 갱신하지 않는다.

import sys
input = sys.stdin.readline
n = int(input())
dp = {n:[n]}
queue = [n]
while queue:
    if 1 in dp: break
    x = queue.pop(0)
    if x % 3 == 0 and x // 3 not in dp:
        queue.append(x//3)
        dp[x // 3] = dp[x] + [x // 3]
    if x % 2 == 0 and x // 2 not in dp:
        queue.append(x//2)
        dp[x // 2] = dp[x] + [x // 2]
    if x - 1 not in dp:
        queue.append(x - 1)
        dp[x - 1] = dp[x] + [x - 1]
print(len(dp[1])-1)
print(*dp[1])

# 다른사람코드
# 재귀를 이용해 dp를 만들면서 최소값을 출력하고 dp를 바탕으로 다시 시행단계를 계산해서 출력한다.
# 실행시간이 더 줄어든다. 

save={1:0,2:1}
def func(n):
    if n in save.keys():
        return save[n]
    m=min(func(n//2)+1+n%2,func(n//3)+1+n%3)
    save[n]=m
    return m
n=int(input())
print(func(n))
m=n
ans=[n]
while m>1:
    if save[m]==save[m//2]+1+m%2:
        if m%2:
            m-=1
            ans.append(m)
        m//=2
        ans.append(m)
    else:
        while m%3:
            m-=1
            ans.append(m)
        m//=3
        ans.append(m)
print(*ans)
