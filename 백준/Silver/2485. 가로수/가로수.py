import sys
import math
input = sys.stdin.readline

N = int(input().rstrip())
arr=[]
for _ in range(N):
    num = int(input().rstrip())
    arr.append(num)

differences = []
for i in range(1, len(arr)):
    differences.append(arr[i] - arr[i-1])

main_gcd = differences[0]
for i in range(1, len(differences)):
    main_gcd = math.gcd(main_gcd, differences[i])
    
result = 0
for diff in differences:
    result += diff // main_gcd - 1
    
print(result)

