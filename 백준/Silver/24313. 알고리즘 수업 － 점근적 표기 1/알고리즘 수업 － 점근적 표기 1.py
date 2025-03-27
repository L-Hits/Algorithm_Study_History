a,b = map(int, input().split())
i= int(input())
j= int(input())

for k in range(j, 100):
  if not (a*k+b <= i*k):
    print(0)
    break
else:
  print(1)