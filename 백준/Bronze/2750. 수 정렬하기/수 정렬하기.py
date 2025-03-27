count = int(input())
arr = []
for i in range(count):
  arr.append(int(input()))
  
arr.sort()
for i in arr:
  print(i)