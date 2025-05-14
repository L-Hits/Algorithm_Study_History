import sys
input = sys.stdin.readline

me = input().strip()
doctor = input().strip()
if len(me) >= len(doctor):
    print('go')
else:
    print('no')