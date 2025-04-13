import sys
input = sys.stdin.readline

k = int(input().strip())
Num = []
for _ in range(k):
    n = int(input().strip())
    if n == 0:
        Num.pop()
    else:
        Num.append(n)

print(sum(Num))

