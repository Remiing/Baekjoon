import sys
input = sys.stdin.readline
N = int(input())
video = [list(input().rstrip()) for _ in range(N)]
def zip(x,y,n):
    if n==1:
        return(video[x][y])
    check = video[x][y]
    for i in range(n):
        for j in range(n):
            if check != video[x+i][y+j]:
                k = n//2
                lu = zip(x,y,k)
                ru = zip(x,y+k,k)
                ld = zip(x+k,y,k)
                rd = zip(x+k,y+k,k)
                return(f'({lu}{ru}{ld}{rd})')
    return(check)

print(zip(0,0,N))
            
