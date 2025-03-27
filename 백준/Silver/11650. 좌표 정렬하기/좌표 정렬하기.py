N = int(input())
pointer =[]
for i in range(N):
    pointer.append(list(map(int,input().split())))

pointer.sort(key=lambda x: (x[0],x[1]))

for arr in pointer:
    print(arr[0], arr[1])