import sys
input = sys.stdin.readline

A, B, C= map(int, input().strip().split())

print((B//A)*C*3)
