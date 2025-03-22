count = int(input())
result = list([0] * 100 for _ in range(100))

for i in range(count):
  x, y = map(int,input().split())
  for a in range(x, x+10):
    for b in range(y, y+10):
      if result[a][b] == 0:
        result[a][b] = 1

print(sum(arr.count(1) for arr in result))