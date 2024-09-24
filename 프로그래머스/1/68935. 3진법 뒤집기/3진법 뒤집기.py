def solution(n):
    num3 = ''
    
    while n >= 3:    
        num3 += str(n % 3)
        n //= 3
    num3 += str(n)
    
    print(num3)
    return int(num3, 3)
