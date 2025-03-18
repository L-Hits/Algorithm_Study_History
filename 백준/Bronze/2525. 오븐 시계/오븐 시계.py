h,m = map(int, input().split())
timer = int(input())

h += (m + timer) // 60
m = (m + timer) % 60

if h >= 24:
    h %= 24
    
print(h, m)