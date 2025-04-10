import sys
input = sys.stdin.readline

N = int(input().strip())

# 1주 604800

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(N) // 604800)
