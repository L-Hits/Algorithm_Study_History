import sys
input = sys.stdin.readline
import math
arr =[]
for _ in range(2):
    A,B = map(int, input().split())
    arr.append(A)
    arr.append(B)


result_A = arr[0]*arr[3] + arr[1]*arr[2]
result_B = arr[1] * arr[3]
gcd_num = math.gcd(result_A, result_B)

while gcd_num != 1:
    result_A //= gcd_num
    result_B //= gcd_num
    gcd_num = math.gcd(result_A, result_B)
print(result_A, result_B)


