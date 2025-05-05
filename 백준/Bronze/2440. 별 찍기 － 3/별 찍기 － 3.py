import sys
input = sys.stdin.readline

N = int(input().strip())
STR = ''
for i in range(N, 0, -1):
    STR = '*' * i
    print(STR)
