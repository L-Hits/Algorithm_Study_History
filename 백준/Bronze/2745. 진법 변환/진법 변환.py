num, B = input().split()
result = 0

for i in range(len(num)):
  if num[i].isdigit():
    result += int(num[i]) * (int(B) ** (len(num) - i - 1))
  else:
    result += (ord(num[i]) - 55) * (int(B) ** (len(num) - i - 1))
print(result)