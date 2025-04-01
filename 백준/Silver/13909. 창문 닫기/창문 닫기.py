import sys
input = sys.stdin.readline

N = int(input().rstrip())

count = 0
i = 1
while i * i <= N:
    count += 1
    i += 1

print(count)