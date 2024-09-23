def solution(s):
    answer = 0
    
    result = list(s)
    if result[0] == '-':
        result.remove('-')
        return -1 * int(''.join(result))
    else:
        return int(''.join(result))
    
  