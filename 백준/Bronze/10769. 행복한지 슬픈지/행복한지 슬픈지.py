import sys
input = sys.stdin.readline

strInput = input().strip()

happy = strInput.count(":-)")
sad = strInput.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")