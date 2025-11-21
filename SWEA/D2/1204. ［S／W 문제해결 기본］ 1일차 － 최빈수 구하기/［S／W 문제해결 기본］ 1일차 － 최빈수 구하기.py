from collections import Counter

testCase = int(input())
for i in range(1, testCase+1):
    _ = int(input())
    arr = list(map(int, input().split()))
    commonDict = Counter(arr)
    maxCount = max(commonDict.values())

    result = max([num for num, count in commonDict.items() if count == maxCount])

    print(f'#{i} {result}')
