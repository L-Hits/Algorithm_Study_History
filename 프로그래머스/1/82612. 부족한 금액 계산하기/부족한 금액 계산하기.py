def solution(price, money, count):
    
    need_money = 0
    now_count = 1
    
    for i in range(count):
        need_money += price * now_count
        now_count += 1
        
    if need_money - money < 0:
        return 0
    else:
        return need_money - money
        
