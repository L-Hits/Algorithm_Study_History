box, count = map(int, input().split())
arr = [i for i in range(1, box+1)]

for _ in range(count):
    a, b = map(int, input().split())
    arr[a-1:b] = arr[a-1:b][::-1]
    
for i in arr:
    print(i, end=' ')