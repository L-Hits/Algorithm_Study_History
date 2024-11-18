def solution(s):
    answer = []
    answer_word = []
    join_str= ''
    str = s.split(' ')
    
    
    for i in str:
        for j in range(len(i)):
            if j % 2 == 0:  #짝수 번째는 대문자
                answer_word.append(i[j].upper())
            else:           #홀수 번째는 소문자 혹은 공백
                answer_word.append(i[j].lower())
                
        answer_word += " "
        join_str = "".join(answer_word)
        
    # 마지막 공백 제거 (조건적으로)
    if join_str.endswith(" "):
        join_str = join_str[:-1]
        
    return join_str