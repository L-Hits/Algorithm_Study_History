num = 0
nums = []
while True:
  num = int(input())
  if num == -1:
    break
  nums.append(num)

for num in nums:
  divisors = [i for i in range(1, num) if num % i == 0]
  if sum(divisors) == num:
    print(num, "=", " + ".join(map(str, divisors[::1])))
  else:
    print(num, "is NOT perfect.")
