def solution(n):
    answer = list(map(int, str(n)))
    answer.sort()
    answer.reverse()
    
    return int(''.join(map(str, answer)))