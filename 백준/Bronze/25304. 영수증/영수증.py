result_money = int(input())
count = int(input())
sum = 0
for i in range(count):
    a,b = map(int, input().split())
    sum += a * b

if result_money == sum:
    print("Yes")
else:
    print("No")