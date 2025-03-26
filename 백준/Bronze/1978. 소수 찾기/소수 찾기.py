count = int(input())
result = 0
arr = list(map(int, input().split()))

for i in range(count):
    num = arr[i]
    if num < 2:
      continue
    isPrime = True
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
          isPrime = False
          break
    if isPrime:
      result += 1
            
print(result)
