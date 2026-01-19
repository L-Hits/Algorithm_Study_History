testCase = int(input())

for _ in range(testCase):
    a, b = map(int, input().split())
    a = a % 10
    
    exp = b % 4
    if exp == 0:
        exp = 4
    
    result = (a ** exp) % 10
    if result == 0:
        print(10)
    else:
        print(result)