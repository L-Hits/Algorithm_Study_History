import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return True
    if n <= 1:
        return False
    
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if arr[i]:
            for j in range(i*i, n+1, i):
                arr[j] = False
    
    return arr[n]

def calculate_word_value(word):
    total = 0
    for char in word:
        if 'a' <= char <= 'z':
            total += ord(char) - ord('a') + 1
        elif 'A' <= char <= 'Z':
            total += ord(char) - ord('A') + 27
    return total


word = input().strip()
word_value = calculate_word_value(word)

if is_prime(word_value):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
