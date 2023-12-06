import re
from pprint import pprint as pp
test_data="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def generate_empty_dict(up_to_number):
    empty_dict = {key: {"copies":1, "points": 0} for key in range(1, up_to_number + 1)}
    return empty_dict

def parse_data(data: str) -> list:
    '''Parses the data.'''
    cards = []
    points = 0
    scratch_cards = generate_empty_dict(len(data))
    #print(scratch_cards)
    for ctr, line in enumerate(data):
        card_line = line.split(": ")
        winning_numbers = card_line[1].split('|')[0].split()
        my_card = card_line[1].split('|')[1].split()
        cards.append((winning_numbers, my_card))
        my_win = set(winning_numbers).intersection(my_card)
        if len(my_win) > 0:
            points += 2**(len(my_win)-1)
            scratch_cards[ctr+1]["points"] += len(my_win)
    sum_cards = 0
    for i in scratch_cards:
        for x in range(scratch_cards[i]["points"]):
            scratch_cards[i+x+1]["copies"] += scratch_cards[i]["copies"]
        sum_cards += scratch_cards[i]["copies"]
    return points, sum_cards

with open("inputs.txt", "r") as f:
    data = f.readlines()

points, sum_cards = parse_data(test_data.splitlines())

pp(points)
pp(sum_cards)

points, sum_cards = parse_data(data)

pp(points)
pp(sum_cards)