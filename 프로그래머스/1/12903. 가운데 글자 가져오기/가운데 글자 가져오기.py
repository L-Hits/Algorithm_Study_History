def solution(s):
    answer = ''
    middle_len = int(len(s) / 2)
    
    if len(s) % 2 == 0: #짝수
        return s[middle_len-1:middle_len+1]
    else:   #홀수
        return s[middle_len]
        
    