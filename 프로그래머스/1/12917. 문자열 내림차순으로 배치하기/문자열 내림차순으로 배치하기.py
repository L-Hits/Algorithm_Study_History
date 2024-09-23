def solution(s):
    new_s =list(map(str,s))
    new_s.sort()
    new_s.reverse()
    
    return ''.join(new_s)