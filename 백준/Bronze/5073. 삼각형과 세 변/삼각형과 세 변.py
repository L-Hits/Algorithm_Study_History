results = []

while True:
  a, b, c = map(int, input().split())
  arr = [a, b, c]
  arr.sort()
  if a == b == c == 0:
    break
  if arr[0] + arr[1] <= arr[2]:
    results.append("Invalid")
  elif a == b == c:
    results.append("Equilateral")
  elif a == b or b == c or a == c:
    results.append("Isosceles")
  else:
    results.append("Scalene")

for result in results:
  print(result)