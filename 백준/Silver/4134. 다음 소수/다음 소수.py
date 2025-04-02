import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

result = []
n = int(input().rstrip())
for _ in range(n):
    num = int(input().rstrip())
    while True:
        if is_prime(num):
            result.append(num)
            break
        else:
            num += 1

print('\n'.join(map(str, result)))
        
        