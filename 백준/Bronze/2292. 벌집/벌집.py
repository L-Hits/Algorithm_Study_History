n = int(input())
last_room = 1     
result = 1    

while n > last_room:
    last_room += 6 * result
    result += 1

print(result)