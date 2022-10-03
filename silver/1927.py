import sys
N = int(sys.stdin.readline().rstrip())
heap = [None]
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heap.append(x)
        i = len(heap)-1
        while i > 1 and heap[i] < heap[i//2]:
            heap[i], heap[i//2] = heap[i//2], heap[i]
            i = i//2
    else:
        if len(heap) == 1: print(0)
        else:
            heap[1], heap[-1] = heap[-1], heap[1]
            print(heap.pop())
            point = 1
            while len(heap) > 1:
                small = point
                if point*2 < len(heap) and heap[point*2] < heap[small]:
                    small = point*2
                if point*2+1 < len(heap) and heap[point*2+1] < heap[small]:
                    small = point*2+1
                if point != small:
                    heap[point], heap[small] = heap[small], heap[point]
                    point = small
                else:
                    break


# heapq 사용
import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    print(heap)
