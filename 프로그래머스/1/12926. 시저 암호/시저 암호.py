def solution(s, n):
    answer = ''
    #65 ~ 90 대문자
    #97 ~ 122 소문자
    
    char_list = list(s)

    for i in range(len(char_list)):
        if char_list[i] != ' ': #문자인 경우
            if ord(char_list[i]) >= 65 and ord(char_list[i]) <= 90: #대문자인 경우
                if (ord(char_list[i]) + n) > 90:
                    char_list[i] = chr((ord(char_list[i]) + n) - 26)
                else:
                    char_list[i] = chr((ord(char_list[i]) + n))
                
            else: #소문자인 경우
                if (ord(char_list[i]) + n) > 122:
                    char_list[i] = chr((ord(char_list[i]) + n) - 26)
                else:
                    char_list[i] = chr((ord(char_list[i]) + n))
            
    answer = "".join(char_list)
    return answer