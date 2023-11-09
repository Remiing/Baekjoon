# https://school.programmers.co.kr/learn/courses/30/lessons/150368

# 각 이모티콘 할인율의 모든 조합을 구한 뒤, 그 조합에서의 이모티콘 플러스 서비스 가입자, 이모티콘 판매액을 계산합니다. 
# 보통 모든 조합을 구하면 시간이 굉장히 오래걸리지만, 이 문제의 경우 이모티콘의 개수 7개, 할인율 10%, 20%, 30%, 40% 4가지로 최대 4^7=16,384가지의 경우만 보면 됩니다. 

# 각 조합마다 임시로 [서비스 가입자, 판매액]을 구하고, 기존 answer에 저장된 서비스 가입자보다 많거나, 서비스 가입자가 같고 판매액이 높을 때 갱신합니다. 

# 단순히 이모티콘 원가에 0.9, 0.8, 0.7, 0.6을 곱해서 할인된 가격을 구할 수 있지만 부동소수점 문제가 발생해서 int(b*(100-a)/100)로 읽기 쉽게 표현했습니다.

def solution(users, emoticons):
    from itertools import product
    answer = [0, 0]
    
    for prod in product([10, 20, 30, 40], repeat=len(emoticons)):
        temp_answer = [0, 0]
        for user in users:
            sum_price = sum([int(b*(100-a)/100) for a, b in zip(prod, emoticons) if a >= user[0]])
            if sum_price >= user[1]:
                temp_answer[0] += 1
            else:
                temp_answer[1] += sum_price
                
        if temp_answer[0] > answer[0] or (temp_answer[0] == answer[0] and temp_answer[1] > answer[1]):
            answer = temp_answer[:]
            
    return answer
  
