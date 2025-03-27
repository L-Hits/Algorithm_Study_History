N = int(input())
count = 0
number = 1
while count < N:
  if number.__str__().count('666') > 0:
    count += 1
  number += 1
  
print(number-1)