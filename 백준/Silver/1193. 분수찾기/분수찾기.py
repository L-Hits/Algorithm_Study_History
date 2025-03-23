num = int(input())
line = 1
sum = 0

while sum < num:
    sum += line
    line += 1

result_line = line - 1
line_endNum = result_line * (result_line + 1) // 2

if result_line % 2 == 0:
    L, R = result_line, 1
    for _ in range(line_endNum - num):
        L -= 1
        R += 1
else:
    L, R = 1, result_line
    for _ in range(line_endNum - num):
        L += 1
        R -= 1

print(f'{L}/{R}')
