import sys
com_num = int(sys.stdin.readline().rstrip())
connect_num = int(sys.stdin.readline().rstrip())
lines = list([sys.stdin.readline().rstrip() for _ in range(connect_num)])
virus = []
queue = [1]
connect_list = [[] for _ in range(com_num+1)]
for i in lines:
    cn1, cn2 = map(int, i.split())
    connect_list[cn1].append(cn2)
    connect_list[cn2].append(cn1)
while queue:
    for _ in queue:
        queue.extend([x for x in connect_list[queue[0]] if x not in virus and x not in queue])
        virus.append(queue[0])
        del queue[0]
print(len(virus)-1)


#다른사람풀
import sys
n = int(input())
l = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)
visited = [0] * (n + 1)
st = [1]
while st:
    a = st.pop()
    if not visited[a]:
        visited[a] = 1
        st += l[a]
print(sum(visited) - 1)
