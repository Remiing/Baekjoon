# 입력이 들어온대로 이진트리 딕셔너리를 만든다.
# 결과값 문자열에 A를 넣고 딕셔너리를 돌면서 노드를 추가한다.
# 전위 순회라면 문자열 A를 ABC로 바꾸고 중위 순회라면 A를 BAC, 후위 순회라면 BCA로 바꾼다.
# ex) 전위순회 A > ABC > ABDC > ABDCEF > ABDCEFG
# ex) 중위순회 A > BAC > DBAC > DBAECF > DBAECFG
# ex) 후위순회 A > BCA > DBCA > DBEFCA > DBEGFCA

import sys
input = sys.stdin.readline
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = left.rstrip('.'), right.rstrip('.')
preorder, inorder, postorder = 'A', 'A', 'A'
for key, value in tree.items():
    preorder = preorder.replace(key, key+value[0]+value[1])
    inorder = inorder.replace(key, value[0]+key+value[1])
    postorder = postorder.replace(key, value[0]+value[1]+key)

print(preorder)
print(inorder)
print(postorder)

# https://www.acmicpc.net/source/53985916
# 재귀함수로 구현했다.

import sys
input = sys.stdin.readline

def pre_order(r):
    if r == '.': return
    print(r, end='')
    pre_order(d[r][0])
    pre_order(d[r][1])

def in_order(r):
    if r == '.': return
    in_order(d[r][0])
    print(r, end='')
    in_order(d[r][1])

def post_order(r):
    if r == '.':return
    post_order(d[r][0])
    post_order(d[r][1])
    print(r, end='')

N = int(input())
d = {}
for _ in range(N):
    Root, Left, Right = input().split()
    d[Root] = [Left, Right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')
