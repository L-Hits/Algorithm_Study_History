import sys
input = sys.stdin.readline
result = []
while True:
    input_data = input().strip()
    if input_data == '0':
        break
    
    N, P = map(int, input_data.split())
    
    if P % 2 == 1:
        pair_page = P + 1
        other_pair1 = N - P + 1
        other_pair2 = N - P
    else:
        pair_page = P - 1
        other_pair1 = N - P + 2
        other_pair2 = N - P + 1
    
    result.append([pair_page, other_pair1, other_pair2])

for i in range(len(result)):
    print(" ".join(map(str, sorted(result[i]))))