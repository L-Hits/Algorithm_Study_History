import sys
input = sys.stdin.readline

n,c = map(int, input().split())
hh = 0
mm = 0
ss = 0

for i in range(n):
    m,s = map(int, input().split(":"))
    mm += m
    ss += s
     
if n == 1:
    hh = mm // 60
    mm = mm % 60
    ss = ss % 60
else:
    ss -= c * (n-1)
    mm += ss // 60
    hh += mm // 60
    mm = mm % 60
    ss = ss % 60
    
print(f"{hh:02}:{mm:02}:{ss:02}")
