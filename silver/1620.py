import sys

input = sys.stdin.readline
N, M = map(int, input().split())

pokedex_str, pokedex_int = {}, {}
for i in range(1, N+1):
    pokemon = input().rstrip()
    pokedex_str[pokemon] = i
    pokedex_int[i] = pokemon

for _ in range(M):
    question = input().rstrip()
    if question.isdecimal():
        print(pokedex_int[int(question)])
    else:
        print(pokedex_str[question])

# 리스트 하나에 순서대로 입력받아 도감을 만든 후 숫자를 입력받으면 pokedex[i], 문자를 입력받으면 pokedex.index(s) 하려고 했으나 시간초과가 떴다.
# 문자:숫자, 숫자:문자로 연결된 딕셔너리 두개를 만들어서 해결했다.

# else code

import sys

lines = sys.stdin.buffer.read().decode().splitlines()

n, m = map(int, lines[0].split())
dic = {word: str(idx+1) for idx, word in enumerate(lines[1:n+1])}
answer = '\n'.join(lines[int(line)] if line.isdigit() else dic[line] for line in lines[1 + n:])
print(answer)
