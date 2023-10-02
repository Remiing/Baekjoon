# ex) [[1,2,3,4][5,6,7,8][9,10,11,12][13,14,15,16]]
# turn_list: 처음 리스트의 최외곽부터 돌면서 한줄씩 값을 저장합니다. [[1,2,3,4,8,12,16,15,14,13,9,5],[6,7,11,10]]
# array_seq: 처음 리스트의 최외곽부터 돌면서 array의 각 요소가 몇번째 줄의 몇번째인지 저장합니다. [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 11), (1, 0), (1, 1), (0, 4)], [(0, 10), (1, 3), (1, 2), (0, 5)], [(0, 9), (0, 8), (0, 7), (0, 6)]]
# turn_list의 줄마다 r만큼 회전시킵니다.
# array_seq의 각 요소를 돌면서 turn_list에서 값을 찾아 저장한 뒤 출력합니다.

import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
array = [input().split() for _ in range(n)]
turn_num = min(n, m) // 2
turn_list = [[] for _ in range(turn_num)]
array_seq = [[(0,0)]*m for _ in range(n)]
for tn in range(turn_num):
    x, y = tn, tn
    cnt = 0
    for i in range(m-2*tn-1):
        turn_list[tn].append(array[y][x])
        array_seq[y][x] = (tn, cnt)
        x += 1
        cnt += 1
    for i in range(n-2*tn-1):
        turn_list[tn].append(array[y][x])
        array_seq[y][x] = (tn, cnt)
        y += 1
        cnt += 1
    for i in range(m-2*tn-1):
        turn_list[tn].append(array[y][x])
        array_seq[y][x] = (tn, cnt)
        x -= 1
        cnt += 1
    for i in range(n-2*tn-1):
        turn_list[tn].append(array[y][x])
        array_seq[y][x] = (tn, cnt)
        y -= 1
        cnt += 1

for tn in range(turn_num):
    turn_list[tn] = turn_list[tn][r % len(turn_list[tn]):] + turn_list[tn][:r % len(turn_list[tn])]

for i in range(n):
    for j in range(m):
        tn, cnt = array_seq[i][j]
        array[i][j] = turn_list[tn][cnt]

for i in array:
    print(*i)

# 다른사람코드
# 나는 외곽 줄, 위치를 저장해두고 매칭하는 방법으로 풀었는데,
# 최외각을 돌면서 슬라이싱을 통해 q에 값을 넣어두고, r만큼 회전시킨 후 다시 최외곽부터 돌면서 값을 저장합니다.

n, m, r = map(int, input().split())
graph = [list(input().split()) for _ in range(n)]
answer = [[0]*m for _ in range(n)]
q = deque()

for i in range(min(n, m) // 2):
  q.clear()
  q.extend(graph[i][i:m-i]) # 위
  q.extend([row[m-i-1] for row in graph[i+1:n-i-1]]) # 오른쪽
  q.extend(graph[n-i-1][i:m-i][::-1]) # 아래
  q.extend(row[i] for row in graph[i+1:n-i-1][::-1]) # 왼쪽
  q.rotate(-r)

  for j in range(i, m-i):
    answer[i][j] = q.popleft()
  for j in range(i+1, n-i-1):
    answer[j][m-i-1] = q.popleft()
  for j in range(m-i-1, i-1, -1):
    answer[n-i-1][j] = q.popleft()
  for j in range(n-i-2, i, -1):
    answer[j][i] = q.popleft()

for line in answer:
  print(" ".join(line))
