from itertools import combinations
import sys
input = sys.stdin.readline
while True:
    test_case = input().split()
    if len(test_case) == 1:
        break
    for com in combinations(test_case[1:], 6):
        print(*com)
    print()






