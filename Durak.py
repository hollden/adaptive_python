deck = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# first_card, second_card = input().split()
# trump = input()
first_card, second_card = '7C', '10H'
trump = 'S'
first_card_weight = deck.index(first_card[:-1]) + first_card.count(trump) * 10
second_card_weight = deck.index(second_card[:-1]) + second_card.count(trump) * 10

if (first_card[-1] == second_card[-1]) or (first_card[-1] == trump or second_card[-1] == trump):

    if first_card_weight > second_card_weight:
        print('First')
    elif first_card_weight < second_card_weight:
        print('Second')
    else:
        print('Error')
# elif first_card[1] == trump or second_card[1] == trump:
#     if first_card_weight > second_card_weight:
#         print('First')
#     elif first_card_weight < second_card_weight:
#         print('Second')
#     else:
#         print('Error')

else:
    print('Error')


