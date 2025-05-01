import sys
input = sys.stdin.readline

K, N, M = map(int, input().strip().split())


if K * N < M:
    print(0)
else:
    print(K * N - M)