N,M = map(int, input().split())
board = [list(input()) for _ in range(N)]
min_count = 64 # 최대 값으로 초기화

for i in range(N-7):
  for j in range(M-7):
    count = 0
    for x in range(i, i+8):
      for y in range(j, j+8):
        if (x+y) % 2 == 0:
          if board[x][y] == 'W':
            count += 1
        else:
          if board[x][y] == 'B':
            count += 1
            
    count = min(count, 64-count) # 처음이 B인 경우와, W인인 경우 중 비교
    min_count = min(min_count, count)
      
print(min_count)