arr_x = []
arr_y = []
for _ in range(3):
  a, b = map(int, input().split())
  arr_x.append(a)
  arr_y.append(b)

X = [x for x in arr_x if arr_x.count(x) == 1][0]
Y = [y for y in arr_y if arr_y.count(y) == 1][0]
print(X, Y)
