case_count = int(input())
for _ in range(case_count):
    money = int(input())
    Quarter = money // 25
    money %= 25
    Dime = money // 10
    money %= 10
    Nickel = money // 5
    money %= 5
    Penny = money
    print(Quarter, Dime, Nickel, Penny)