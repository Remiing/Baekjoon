n = list(map(int, input().split()))
print(sum([x*x for x in n])%10)
