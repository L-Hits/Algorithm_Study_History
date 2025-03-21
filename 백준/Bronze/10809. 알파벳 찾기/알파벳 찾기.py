str = input()

for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    if char in str:
        if i == ord('z'):
            print(f"{str.index(char)}")
        else:
            print(f"{str.index(char)}", end=" ")
    else:
        if i == ord('z'):
            print("-1")
        else:
            print("-1", end=" ")