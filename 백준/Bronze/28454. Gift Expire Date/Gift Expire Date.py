import sys
input = sys.stdin.readline

today_Y, today_M, today_D = map(int, input().strip().split("-"))
N = int(input().strip())
gift = [input().strip() for _ in range(N)]
result = 0

for gift_day in gift:
  gift_day_Y, gift_day_M, gift_day_D = map(int, gift_day.split("-"))
  if (today_Y, today_M, today_D) <= (gift_day_Y, gift_day_M, gift_day_D):
    result += 1
    
print(result)

