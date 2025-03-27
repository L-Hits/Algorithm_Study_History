KG = int(input())
count = 0

while KG > 0:
  if KG % 5 == 0:
    count += (KG/5)
    break
  KG -= 3
  count += 1
if KG < 0:
  print(-1)
else:
  print(int(count))
  