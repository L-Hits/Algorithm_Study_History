def solution(left, right):
    answer = 0
    count = 0
    for i in range(left, right+1):
        for j in range(2,i+1): #2부터 시작했으니 1 더해줘야함
            if i % j == 0:#나누어 떨어지면 그 수는 약수
                count += 1
        
        if (count+1) % 2 == 0: #약수의 개수가 짝수면
            answer += i
        else:
            answer -= i
            
        count = 0   #0으로 초기화
    
    return answer