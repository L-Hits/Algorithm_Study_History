import sys
input = sys.stdin.readline

S = input().rstrip()

S_arr = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        S_arr.add(S[i:j])

print(len(S_arr))