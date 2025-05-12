import sys
input = sys.stdin.readline

X = input().strip()  # 문자열로 입력받음
if len(X) == 1:  # 이미 한 자리 수면
    newY = int(X)
    count = 0
else:
    newY = sum(map(int, X))
    count = 1

while newY >= 10:  # 한 자리 수가 될 때까지 반복
    count += 1
    newY = sum(map(int, str(newY)))

print(count)
if newY % 3 == 0:
    print("YES")
else:
    print("NO")