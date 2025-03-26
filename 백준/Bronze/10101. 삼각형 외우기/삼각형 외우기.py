triangle = []

for _ in range(3):
  triangle.append(int(input()))

if sum(triangle) == 180:
  if triangle.count(60) == 3:
    print("Equilateral")
  elif len(set(triangle)) == 2:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")