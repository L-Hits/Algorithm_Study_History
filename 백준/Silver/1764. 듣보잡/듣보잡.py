import sys
input = sys.stdin.readline

N,M = map(int, input().split())
dict = {}
Names=set()

for _ in range(N):
    name = input().rstrip()
    if name in dict:
        dict[name] += 1
    else:
        dict[name] = 1
        Names.add(name)
        
for _ in range(M):
    name = input().rstrip()
    if name in dict:
        dict[name] += 1
    else:
        dict[name] = 1
        Names.add(name)


count = 0
result = []
for name in Names:
    if dict[name] > 1:
        count += 1
        result.append(name)

print(count)
print("\n".join(sorted(result)))
