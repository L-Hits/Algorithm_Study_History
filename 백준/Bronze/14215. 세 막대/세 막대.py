a, b, c = map(int, input().split())
arr = [a,b,c]
arr.sort()

while arr[2] >= arr[1] + arr[0]:
  arr[2] -= 1
print(sum(arr))