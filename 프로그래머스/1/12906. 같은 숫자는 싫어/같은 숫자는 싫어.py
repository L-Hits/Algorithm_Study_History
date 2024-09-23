def solution(arr):
    answer = []
    same_num = arr[0]
    answer.append(arr[0])
    
    for i in range(len(arr)):
        if arr[i] != same_num:
            same_num = arr[i]
            answer.append(arr[i])
    
    return answer