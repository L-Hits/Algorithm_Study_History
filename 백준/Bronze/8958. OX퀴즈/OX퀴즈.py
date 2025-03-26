count = int(input())
score = 0
for i in range(count):
  Continuous = 1
  strs = input()
  for j in range(0, len(strs)):
    if strs[j] == "O":
      score += Continuous
      Continuous += 1
    elif strs[j] == "X":
      Continuous = 1
  print(score)
  score = 0