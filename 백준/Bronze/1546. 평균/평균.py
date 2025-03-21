count = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
sum = 0
for i in range(len(numbers)):
    numbers[i] = numbers[i] / numbers[-1] * 100
    sum += numbers[i]
print(sum/count)