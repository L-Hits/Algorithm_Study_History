count, num = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(count):
    if arr[i] < num:
        print(arr[i], end=' ')