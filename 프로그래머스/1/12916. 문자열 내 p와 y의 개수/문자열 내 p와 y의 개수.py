def solution(s):
    s = s.replace('p', 'P') # p -> P 
    s = s.replace('y', 'Y') # y -> Y

    p_num = s.count('P')
    y_num = s.count('Y')

    print(f"{p_num}, {y_num}")
    return p_num == y_num

    