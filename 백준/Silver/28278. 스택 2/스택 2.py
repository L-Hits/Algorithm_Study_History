import sys
input = sys.stdin.readline

stack_arr = []
result = []
N = int(input().strip())

def stack(option):
    if option == 2:
        if len(stack_arr) == 0:
            result.append(-1)
        else:
            result.append(stack_arr.pop())
            
    elif option == 3:
        result.append(len(stack_arr))
        
    elif option == 4:
        if len(stack_arr) == 0:
            result.append(1)
        else:
            result.append(0)
        
    elif option == 5:
        if len(stack_arr) == 0:
            result.append(-1)
        else:
            result.append(stack_arr[-1])

for _ in range(N):
    option = 0
    input_str = input().strip()
    if len(input_str) != 1:
        option, num = map(int, input_str.split())
        stack_arr.append(num)
    else:
        option = int(input_str)
        stack(option)
        
print("\n".join(list(map(str, result))))
        
    