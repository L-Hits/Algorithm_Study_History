M_card_num = int(input())
M_card = set(map(int, input().split()))

N_card_num = int(input())
N_card = list(map(int, input().split()))

for card in N_card:
    if card in M_card:
        print("1", end=" ")
    else:
        print("0", end=" ")