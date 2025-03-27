N = input()
arr = []
for i in range(len(N)):
    arr.append(int(N[i]))
arr.sort()
arr.reverse()
for i in range(len(arr)):
    print(arr[i], end='')