def solution(d, budget):
    answer = 0
    
#     d.sort()
    
#     for i in d:
#         if budget-i >= 0:
#             budget -= i
#             answer += 1
#             if budget == 0:
#                 return answer
#         else:
#             return answer

    d.sort()
    
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            answer += 1
    
    return answer
            
            
            