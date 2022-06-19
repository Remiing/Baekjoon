import sys
M = int(sys.stdin.readline().strip())
S = set()
for i in range(M):
    command = sys.stdin.readline().strip()
    if ' ' in command:
        command, n = command.split()
        n = int(n)
    if command == 'add':
        S.add(n)
    elif command == 'remove':
        S.discard(n)
    elif command == 'check':
        print(1 if n in S else 0)
    elif command == 'toggle':
        S.discard(n) if n in S else S.add(n)
    elif command == 'all':
        S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    else:
        S = set()

