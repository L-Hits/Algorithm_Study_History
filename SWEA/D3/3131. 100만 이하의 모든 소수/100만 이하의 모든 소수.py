def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

result =[]

for i in range(1, (10**6)+1):
  if isPrime(i):
    result.append(i)
    
print(" ".join(map(str, result)))