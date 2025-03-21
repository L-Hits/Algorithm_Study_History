count = int(input())
for _ in range(count):
    a, b = input().split()
    a = int(a)
    for j in range(len(b)):
        print(b[j] * a, end='')
    print()