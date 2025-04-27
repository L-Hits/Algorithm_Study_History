import sys
input = sys.stdin.readline

N = int(input().strip())
base = 1
result = '0.'
while True:
    base *= 10
    result += str(base // (2**N))
    base %= (2**N)
    
    if base == 0:
        break

print(result)