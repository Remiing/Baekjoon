# 문제의 요지는 카드 중에서 가장 작은 두 수를 찾는 것입니다.
# 따라서 입력받은 cards 리스트를 최소힙으로 만들고 가장 작은 두 개의 값을 꺼내 더한다음 두 번 넣습니다. 

import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
for _ in range(m):
    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    heapq.heappush(cards, num1 + num2)
    heapq.heappush(cards, num1 + num2)
print(sum(cards))









