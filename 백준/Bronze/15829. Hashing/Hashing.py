L = int(input())
str = input()
result = 0
for i in range(L):
    result += (ord(str[i]) - ord('a') + 1) * (31 ** i)
    
print(result % 1234567891)