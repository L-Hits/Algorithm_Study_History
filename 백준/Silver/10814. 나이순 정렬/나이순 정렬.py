N = int(input())
ageAndName =[]
for i in range(N):
    ageAndName.append(list(map(str, input().split())))

ageAndName.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(ageAndName[i][0], ageAndName[i][1])