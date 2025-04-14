import sys 
input = sys.stdin.readline

apple, banana = map(int, input().strip().split())

forMax = min(apple, banana)

for i in range(1, forMax + 1):
    if apple % i == 0 and banana % i == 0:
        print(i, apple // i, banana // i)