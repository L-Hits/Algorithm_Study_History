import sys
input = sys.stdin.readline
import math

result = []
T = int(input().rstrip())
for _ in range(T):
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    result.append(gcd * (A // gcd) * (B // gcd))

for num in result:
    print(num)