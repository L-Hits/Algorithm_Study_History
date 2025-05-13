import sys
input = sys.stdin.readline

N = int(input().strip()) 
students = []  

for _ in range(N):
    students.append(list(map(int, input().strip().split())))

same_class_count = [0] * N

for i in range(N): 
    same_class_students = set()
    
    for grade in range(5): 
        for j in range(N): 
            if i == j:
                continue
            if students[i][grade] == students[j][grade]:
                same_class_students.add(j)
    
    same_class_count[i] = len(same_class_students)

max_count = max(same_class_count)
temp_president = same_class_count.index(max_count) + 1

print(temp_president)