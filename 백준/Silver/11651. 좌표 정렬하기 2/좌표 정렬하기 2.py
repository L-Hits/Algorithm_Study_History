N = int(input())
pointer =[]
for i in range(N):
    pointer.append(list(map(int,input().split())))

pointer.sort(key=lambda x: (x[1],x[0]))

for arr in pointer:
    print(arr[0], arr[1])