import sys
input = sys.stdin.readline

A, B = map(int, input().split())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

AmB = set(A_arr) - set(B_arr)
BmA = set(B_arr) - set(A_arr)

print(len(AmB) + len(BmA))