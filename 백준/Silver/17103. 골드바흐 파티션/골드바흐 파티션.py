import sys
input = sys.stdin.readline

T = int(input().strip())

# 입력값 2 < N <= 1000000
MAX = 1000001
arrPrime = [True] * MAX
arrPrime[0] = arrPrime[1] = False

# 에라토스테네스 체
for i in range(2, int(MAX**0.5)+1):
    if arrPrime[i]:
        for j in range(i*i, MAX, i):
            arrPrime[j] = False

for _ in range(T):
    N = int(input().strip())
    count = 0

    # 절반까지 계산 시 겹치는 일 없음음
    for a in range(2, N//2 + 1):
        if arrPrime[a] and arrPrime[N-a]:
            count += 1
    print(count)    