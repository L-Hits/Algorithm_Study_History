import sys
input = sys.stdin.readline

B_y, B_x = map(int, input().split())
D_y, D_x = map(int, input().split())
Jone_y, Jone_x = map(int, input().split())

dif_D = abs(D_y - Jone_y) + abs(D_x - Jone_x)

diagonal_steps = min(abs(B_y - Jone_y), abs(B_x - Jone_x))  
straight_steps = abs(B_y - Jone_y) + abs(B_x - Jone_x) - 2 * diagonal_steps
dif_B = diagonal_steps + straight_steps


if dif_D < dif_B:
    print("daisy") 
elif dif_D > dif_B:
    print("bessie")
else:
    print("tie")