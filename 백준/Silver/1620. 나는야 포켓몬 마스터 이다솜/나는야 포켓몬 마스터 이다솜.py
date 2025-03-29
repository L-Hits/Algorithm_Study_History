import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
poketmons_nameToNum = {}
poketmons_numToName = {}

for i in range(N):
    name = input().rstrip()
    poketmons_nameToNum[name] = i+1
    poketmons_numToName[i+1] = name

for _ in range(M):
    strOrNum = input().rstrip()
    if strOrNum.isdigit():
        print(poketmons_numToName[int(strOrNum)])
    else:
        print(poketmons_nameToNum[strOrNum])