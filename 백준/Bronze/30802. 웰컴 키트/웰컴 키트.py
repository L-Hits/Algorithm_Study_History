N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())
t_count = 0
for size in arr:
    t_count += (size + T - 1) // T

print(t_count)
print(N // P, N % P)
