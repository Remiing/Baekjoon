# https://school.programmers.co.kr/learn/courses/30/lessons/150369#
# 전체적인 흐름은 가장 먼 집부터 방문하여 가능한만큼 배달하고 수거합니다. 
# 예를 들어 cap=4, deliveries=[1, 0, 3, 1, 2], pickups=[0, 3, 0, 4, 0] 일때
# 첫 번째 과정을 마치면 deliveries=[1, 0, 2, 0, 0], pickups=[0, 3, 0, 0, 0]이 됩니다. 
# 두 번째 과정을 마치면 deliveries=[0, 0, 0, 0, 0], pickups=[0, 0, 0, 0, 0]이 됩니다. 
# 처음으로 5번집까지, 두번째로 3번집까지 왕복하기 때문에 답은 5*2 + 3*2 = 16입니다. 

# 단순히 cap만큼 빼면서 답을 구해도 되지만 cap이 1이라면 시간이 굉장히 오래걸리기 때문에 누적합과 ceil을 통해 왕복횟수를 구했습니다. 
# 예를 들어 deliveries=[1, 0, 3, 1, 2], pickups=[0, 3, 0, 4, 0] 일때
# 배달하기 위해 왕복해야 하는 횟수는 [2, 2, 2, 1, 1]
# 수거하기 위해 왕복해야 하는 횟수는 [2, 2, 1, 1, 0]
# 현재 왕복 횟수(current) 0으로 시작하고 가장 먼 집부터 확인하면서 값이 변할때마다 갱신해 답을 구합니다. 

def solution(cap, n, deliveries, pickups):
    from math import ceil
    answer = 0
    
    d_sum, p_sum = 0, 0
    for i in range(n, 0, -1):
        d_sum += deliveries[i-1]
        deliveries[i-1] = ceil(d_sum/cap)
        p_sum += pickups[i-1]
        pickups[i-1] = ceil(p_sum/cap)
    
    current = 0
    for i in range(n, 0, -1):
        num = max(deliveries[i-1], pickups[i-1])
        if num > current:
            answer += 2*i*(num - current)
            current = num
    
    return answer
  
