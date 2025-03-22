str = [0]*5
maxlen = 0
for i in range(5):
  str[i] = input()
  if len(str[i]) > maxlen:
    maxlen = len(str[i])
  if len(str[i]) < maxlen:
    str[i] += ' '*(maxlen-len(str[i]))


result = ''
for j in range(maxlen):
  for i in range(5):
    if j >= len(str[i]) or str[i][j] == ' ':
      continue
    result += str[i][j]
print(result)