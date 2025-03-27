num = int(input())
result = 0

for i in range(1, num):
    s = i + sum(int(d) for d in str(i))
    if s == num:
        result = i
        break

print(result)
