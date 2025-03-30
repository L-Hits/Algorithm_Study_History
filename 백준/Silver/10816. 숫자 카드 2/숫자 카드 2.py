import sys
input = sys.stdin.readline

N = int(input().rstrip())
N_card = list(map(int, input().split()))

dict = {}
for num in N_card:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

M = int(input().rstrip())
M_card = list(map(int, input().split()))

for num in M_card:
    print(dict.get(num, 0), end=' ')
