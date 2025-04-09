import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
useTime = int(input())

# 시간을 초로 변경
all_S = 0
all_S += h * 3600 + m * 60 + s + useTime

H = (all_S // 3600) % 24
M = (all_S % 3600) // 60
S = all_S % 60
print(f"{H} {M} {S}")

