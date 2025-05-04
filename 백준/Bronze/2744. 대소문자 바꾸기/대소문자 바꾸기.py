import sys
input = sys.stdin.readline

STR = input().strip()

for i in range(len(STR)):
    if STR[i].isupper():
        STR = STR[:i] + STR[i].lower() + STR[i+1:]
    elif STR[i].islower():
        STR = STR[:i] + STR[i].upper() + STR[i+1:]

print(STR)
