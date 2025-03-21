box, count = map(int, input().split())
result = list(range(1, box + 1))
for i in range(count):
    a, b = map(int, input().split())
    result[a - 1], result[b - 1] = result[b - 1], result[a - 1]

for i in result:
    print(i, end=' ')