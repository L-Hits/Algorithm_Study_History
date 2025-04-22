import sys
input = sys.stdin.readline

N = int(input().strip())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

if arrA == arrB:
    print(1)
    sys.exit(0)


for i in range(N-1, -1, -1):
    max_index = arrA.index(max(arrA[:i+1]))
    
    if max_index != i:
        arrA[i], arrA[max_index] = arrA[max_index], arrA[i]
        
        if arrA == arrB:
            print(1)
            sys.exit(0)

print(0)