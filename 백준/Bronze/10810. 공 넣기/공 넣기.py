box, count = map(int, input().split())
result = [0] * box
for i in range(count):
    a, b, c = map(int, input().split())
    for j in range(a, b+1):
        result[j-1] = c
        
for k in range(len(result)):
    print(result[k], end=' ')