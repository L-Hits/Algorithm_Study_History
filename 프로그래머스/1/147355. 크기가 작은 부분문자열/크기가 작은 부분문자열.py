def solution(t, p):
    answer = 0
    numarr = []
    
    for i in range(len(t)-len(p)+1):
        numarr.append(t[i:i+len(p)])
    
    for i in numarr:
        if int(i) <= int(p):
            answer += 1
            
    
    return answer