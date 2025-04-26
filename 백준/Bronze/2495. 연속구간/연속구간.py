import sys
input = sys.stdin.readline
result = []

for _ in range(3):
  Max_Continuous = 1
  num = int(input().strip())
  Continue_Count = 1
  for i in range(1, len(str(num))):
    if str(num)[i] == str(num)[i-1]:
      Continue_Count += 1
    else:
      Max_Continuous = max(Max_Continuous, Continue_Count)
      Continue_Count = 1
  
  Max_Continuous = max(Max_Continuous, Continue_Count)
  result.append(Max_Continuous)
  
print('\n'.join(map(str,result)))

