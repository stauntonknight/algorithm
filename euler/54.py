def is_rf(cards):
    suit = {}
    count = {}
    for card in cards:
        count[cards[0:-1]] += 1
        suit[cards[-1]] += 1
    if suit['C'] == 5 or suit['D'] == 5 || suit['H'] == 5 || suit['S'] == 5:
        if cards['

f = open('54.in', 'r')
for line in f:

