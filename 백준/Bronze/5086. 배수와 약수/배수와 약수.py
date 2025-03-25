
arr = []
while True:
  n1, n2 = list(map(int, input().split()))
  if n1 == 0 and n2 == 0:
    break
  arr.append([n1, n2])

for i in arr:
  if i[0] < i[1] and i[1] % i[0] == 0:
    print('factor')
  elif i[0] > i[1] and i[0] % i[1] == 0:
    print('multiple')
  else:
    print('neither')
    