arr_x = []
arr_y = []
count = int(input())
for _ in range(count):
  a, b = map(int, input().split())
  arr_x.append(a)
  arr_y.append(b)

W = max(arr_x) - min(arr_x)
H = max(arr_y) - min(arr_y)
print(W * H)
