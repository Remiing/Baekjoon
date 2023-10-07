number = [True] * (10001)
self_number = []
for i in range(1, 10001):
    if number[i]:
        self_number.append(i)
    n = i
    while i > 0:
        n, i = n + i%10, i//10
    if n < 10001:
        number[n] = False
print(*self_number, sep='\n')







