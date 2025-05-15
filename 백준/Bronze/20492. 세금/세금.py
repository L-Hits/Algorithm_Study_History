import sys
input = sys.stdin.readline

N = int(input().strip())

a_case = int(N * 0.78)
b_case = int(N * 0.80 + (N - N * 0.80) * 0.78)

print(a_case)
print(b_case)
