arr = list([0]* 9 for i in range(9))

for i in range(9):
  arr[i] = list(map(int, input().split()))
  
  
for i in range(9):
  for j in range(9):
    if arr[i][j] == max(map(max, arr)):
      print(max(map(max, arr)))
      print(i+1, j+1)