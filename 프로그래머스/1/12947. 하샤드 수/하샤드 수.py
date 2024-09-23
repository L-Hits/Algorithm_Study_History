def solution(x):
    x_num = sum( list(map(int, str(x))) )
    
    return x % x_num == 0
    
    
