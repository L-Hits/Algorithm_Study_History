import sys
input = sys.stdin.readline

N = int(input().strip())
years = 2024
months = 8
months_passed = 7 * (N - 1)

years += (months + months_passed) // 12
months = (months + months_passed) % 12

if months == 0:
    months = 12
    years -= 1

print(years, months)