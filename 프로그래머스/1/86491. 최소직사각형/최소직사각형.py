def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    arr_0 = [i[0] for i in sizes]
    arr_1 = [i[1] for i in sizes]
    
    answer = max(arr_0) * max(arr_1)
    
    return answer