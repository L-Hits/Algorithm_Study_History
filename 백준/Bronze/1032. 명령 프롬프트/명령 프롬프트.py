import sys
input = sys.stdin.readline

N = int(input().strip())
Previous_String = ''

for _ in range(N):
    if N == 1:
        input_Str = input().strip()
        print(input_Str)
    else:
        if Previous_String == '':
            Previous_String = input().strip()
            continue
        input_Str = input().strip()
        for i in range(len(input_Str)):
            if Previous_String[i] != input_Str[i]:
                Previous_String = Previous_String[:i] + '?' + Previous_String[i+1:]
                
                
print(Previous_String)
        
