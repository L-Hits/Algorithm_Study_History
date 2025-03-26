arr = list(input().split())
all =""
for i in range(8):
  all += arr[i]

if all == "12345678":
  print("ascending")
elif all == "87654321":
  print("descending")
else:
  print("mixed")