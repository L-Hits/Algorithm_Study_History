import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0


for i in range(N-1):
    for j in range(N-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1
            if count == K:
                print(arr[j], arr[j+1])
                sys.exit()
print(-1)
