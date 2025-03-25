num, count = map(int, input().split())

divisors = [i for i in range(1, num + 1) if num % i == 0]

if count > len(divisors):
  print(0)
else:
  print(divisors[count - 1])