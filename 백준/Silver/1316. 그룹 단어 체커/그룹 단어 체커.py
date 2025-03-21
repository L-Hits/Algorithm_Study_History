count = int(input())
result = 0

for _ in range(count):
    word = input()
    isGroup = False
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i + 1:]:
                isGroup = True
                break
    if not isGroup:
        result += 1

print(result)