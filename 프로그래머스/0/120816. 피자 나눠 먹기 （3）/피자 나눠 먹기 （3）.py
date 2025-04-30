def solution(slice, n):
    allSlice = 0
    count = 0
    
    while True:
        if allSlice >= n:
            return count
            break
        count += 1
        allSlice = slice * count
        
    return answer