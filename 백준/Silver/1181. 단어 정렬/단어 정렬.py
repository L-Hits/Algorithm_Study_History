N = int(input())
words =[]
for i in range(N):
    words.append(input())

words.sort(key=lambda x: (len(x), x))

for i in range(N):
    if i == 0 or words[i] != words[i-1]:
        print(words[i])