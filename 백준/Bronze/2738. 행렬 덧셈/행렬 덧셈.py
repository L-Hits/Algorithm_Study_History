n,m = map(int, input().split())
arr1 = [[0] * m for _ in range(n)]
arr2 = [[0] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]

for i in range(n):
  arr1[i] = list(map(int,input().split()))

for j in range(n):
  arr2[j] = list(map(int,input().split()))
  
for i in range(n):
  for j in range(m):
    result[i][j] = arr1[i][j] + arr2[i][j]
    print(result[i][j], end = ' ')
  print()
    