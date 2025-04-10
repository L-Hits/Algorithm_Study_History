import sys
input = sys.stdin.readline

# 에라토스테네스의 체를 사용한 소수 계산
def get_primes(n):
    # 0부터 n까지의 모든 수에 대한 소수 여부를 저장
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    return is_prime

# 최대 입력값을 고려하여 미리 소수 계산
# 제한 1 ≤ n ≤ 123,456
MAX = 123456 * 2 + 1
prime_check = get_primes(MAX)

result = []
while True:
    n = int(input().strip())
    if n == 0:
        break
    
    count = 0
    
    for i in range(n+1, 2*n+1):
        if prime_check[i]:
            count += 1
    
    result.append(count)

print('\n'.join(map(str, result)))