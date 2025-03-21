result = list(range(1, 31))

for _ in range(28):
    num = int(input())
    if num in result:
        result.remove(num)

result.sort()
for i in result:
    print(i)