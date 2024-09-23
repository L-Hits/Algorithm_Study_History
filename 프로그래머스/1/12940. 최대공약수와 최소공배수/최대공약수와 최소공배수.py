import math


def solution(n, m):
    
    least_num = n*m // math.gcd(n,m)
    answer = [math.gcd(n,m), least_num]     #최대공약수는 math써서 gcd(호제법), 최소공배수는 두 수의 곱을                                                 최대공약수로 나눈 몫임
    return answer
   