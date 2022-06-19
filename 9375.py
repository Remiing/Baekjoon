import sys
TestCase = int(sys.stdin.readline().rstrip())
for _ in range(TestCase):
    n = int(sys.stdin.readline().rstrip())
    clothes = {}
    Case = 1
    for _ in range(n):
        cloth_name, cloth_kind = sys.stdin.readline().rstrip().split() 
        if cloth_kind not in clothes:
            clothes[cloth_kind] = 1
        else:
            clothes[cloth_kind] += 1
    for i in clothes.values():
        Case *= (i+1)
    print(Case - 1)
