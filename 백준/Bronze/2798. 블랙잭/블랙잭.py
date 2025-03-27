count, max_num = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = 0
for i in range(count):
  for j in range(i+1, count):
    for k in range(j+1, count):
      sum_num = numbers[i] + numbers[j] + numbers[k]
      if sum_num <= max_num:
        max_sum = max(max_sum, sum_num)

print(max_sum)