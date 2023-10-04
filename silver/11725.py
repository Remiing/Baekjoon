# 입력을 받을 때 딕셔너리로 연결된 노드를 저장합니다. 노드 1부터 시작해서 연결된 노드들에 대해 방문한적이 없는 노드라면 큐에 넣고 부모노드를 갱신합니다.

import sys
input = sys.stdin.readline
n = int(input())
tree_dict = {i: [] for i in range(1, n+1)}
parent = [1]*2 + [0]*(n-1)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree_dict[a].append(b)
    tree_dict[b].append(a)
q = [1]
while q:
    node = q.pop(0)
    for child in tree_dict[node]:
        if not parent[child]:
            parent[child] = node
            q.append(child)
print(*parent[2:], sep='\n')

# 다른사람코드
# 나는 연결된 노드 저장할 때 딕셔너리를 썼는데 모든 노드가 숫자이기 때문에 리스트만 써도 충분했다.
# pop(0) 대신 pop()을 써도 작동한다. 

def main():
    n = int(sys.stdin.readline())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        adj_list[x].append(y)
        adj_list[y].append(x)

    parents = [0 for _ in range(n + 1)]

    stack = [1]
    while stack:
        node = stack.pop()
        for next_node in adj_list[node]:
            if next_node != parents[node]:
                parents[next_node] = node
                stack.append(next_node)
    print(*parents[2:], sep="\n")


if __name__ == "__main__":
    main()
