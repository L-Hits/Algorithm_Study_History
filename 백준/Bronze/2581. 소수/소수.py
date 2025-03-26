start_num = int(input())
end_num = int(input())
result = 0
arr = []

for num in range(start_num, end_num + 1):
    if num < 2:
      continue
    isPrime = True
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
          isPrime = False
          break
    if isPrime:
      arr.append(num)
      
if len(arr) == 0:
  print(-1)
else:
  print(sum(arr))
  print(arr[0])

