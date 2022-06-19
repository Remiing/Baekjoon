word = input().lower()
a = list(set(word))
b = [word.count(x) for x in a]

if b.count(max(b)) >= 2:
    print('?')
else:
    print(a[b.index(max(b))].upper())
