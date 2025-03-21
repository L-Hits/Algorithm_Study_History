dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
str = input()
result = 0
for i in range(len(str)):
    for j in dial:
        if str[i] in j:
            result += dial.index(j)+3
print(result)