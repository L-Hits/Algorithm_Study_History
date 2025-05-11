import sys
input = sys.stdin.readline

N = int(input().strip())
grid = [[' ' for _ in range(N)] for _ in range(N)]

# 테두리 채우기
for i in range(N):
    for j in range(N):
        # 첫 행 또는 마지막 행
        if i == 0 or i == N-1:
            grid[i][j] = '*'
        # 첫 열 또는 마지막 열
        elif j == 0 or j == N-1:
            grid[i][j] = '*'
        # 주 대각선 (좌상단에서 우하단)
        elif i == j:
            grid[i][j] = '*'
        # 부 대각선 (우상단에서 좌하단)
        elif i + j == N-1:
            grid[i][j] = '*'

for row in grid:
    print(''.join(row))