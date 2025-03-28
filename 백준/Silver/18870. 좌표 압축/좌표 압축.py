N = int(input())
arr = list(map(int, input().split()))

set_arr = sorted(list(set(arr)))

dict = {}
for i, value in enumerate(set_arr):
    dict[value] = i

for value in arr:
    print(dict [value], end=' ')