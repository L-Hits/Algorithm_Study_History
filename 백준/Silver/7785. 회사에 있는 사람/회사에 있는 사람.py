import sys
input = sys.stdin.readline

n = int(input())
person = set()

for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        person.add(name)
    else:
        person.remove(name)
    
print("\n".join(sorted(person, reverse=True)))