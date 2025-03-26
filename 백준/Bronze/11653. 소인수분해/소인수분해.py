num = int(input())
arr = []
divisor = 2

while num > 1:
  while num % divisor == 0:
    arr.append(divisor)
    num //= divisor
  divisor += 1

for i in arr:
  print(i)