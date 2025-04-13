import sys
input = sys.stdin.readline

black_point = {"k":0,"p":-1,"n":-3,"b":-3,"r":-5,"q":-9}
white_point = {"K":0,"P":1,"N":3,"B":3,"R":5,"Q":9}

result = 0
chessBorad = []
for _ in range(8):
    chessBorad.append(input().rstrip())

for i in range(8):
    for j in range(8):
        if chessBorad[i][j] in black_point:
            result += black_point[chessBorad[i][j]]
        elif chessBorad[i][j] in white_point:
            result += white_point[chessBorad[i][j]]

print(result)
        