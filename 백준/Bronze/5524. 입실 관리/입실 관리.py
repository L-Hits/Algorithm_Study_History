import sys
input = sys.stdin.readline

N = int(input().strip())
result = []
for _ in range(N):
  inputString = input().strip()
  result.append(inputString.lower())
  
  
for i in range(N):
  print(result[i])