import sys
import math
input = sys.stdin.readline

result = []

while True:
    B, N = map(int, input().strip().split())
    if B == 0 and N == 0:
        break
    
    A_approx = B**(1/N)

    A_floor = int(A_approx)  
    A_ceil = A_floor + 1  
    
    if abs(A_floor**N - B) <= abs(A_ceil**N - B):
        result.append(A_floor)
    else:
        result.append(A_ceil)

for num in result:
    print(num)