from collections import Counter

class Card:
    suite = ''
    value = 0
    def __init__(self, card):
        self.suite = card[1]
        val = card[0]
        if val >= '2' and val <= '9':
            self.value = int(val)
        if val == 'T':
            self.value = 10
        if val == 'J':
            self.value = 11
        if val == 'Q':
            self.value = 12
        if val == 'K':
            self.value = 13
        if val == 'A':
            self.value = 14

class Hand:
    cards = []
    def __init__(self, cards):
        self.cards = cards

    def consecutive(self):
        values = sorted([c.value for c in self.cards])
        for v in range(1, len(values)):
            if values[v] - values[v-1] != 1:
                return False
        return True

    def high_card(self):
        counts = Counter(self.values()).most_common(7)
        max_v = -1
        for c in range(0, len(counts)):
            if counts[c][1] == 1:
                max_v = max(max_v, counts[c][0])
        return max_v


    def same_suite(self):
        return self.num_suites() == 1

    def num_suites(self):
        return len(set([card.suite for card in self.cards]))

    def values(self):
        return [card.value for card in self.cards]

    """ Hand methods.
    """
    def straight(self):
        if self.consecutive():
            return max(self.values())
        return None

    def flush(self):
        if self.same_suite():
            return max(self.values())
        return None

    def straight_flush(self):
        if self.flush() != None and self.straight() != None:
            return self.straight
        return None

    def royal_flush(self):
        return self.straight_flush() and self.high_card() == 13

    def four_of_a_kind(self):
        counts = Counter(self.values()).most_common(1)
        if counts[0][1] == 4:
            return counts[0][0]
        None

    def three_of_a_kind(self):
        counts = Counter(self.values()).most_common(1)
        if counts[0][1] == 3:
            return counts[0][0]
        return None

    def pair(self):
        counts = Counter(self.values()).most_common(1)
        if counts[0][1] == 2:
            return counts[0][0]
        return None

    def two_pairs(self):
        counts = Counter(self.values()).most_common(2)
        if len(counts) != 2:
            return None
        if counts[0][1] == 2 and counts[1][1] == 2:
            return (counts[0][0], counts[1][0])
        return None

    def full_house(self):
        counts = Counter(self.values()).most_common(2)
        if counts[0][1] == 3 and counts[1][1] == 2:
            return (counts[0][0], counts[1][0])
        return None


    """ Score hands.
    """
    def score(self):
       curr_score = []
       curr_score.append(self.high_card())

       pair = self.pair()
       if pair != None:
           curr_score.append(pair)
       else:
           curr_score.append(1)

       two_pairs = self.two_pairs()
       if two_pairs != None:
           a = two_pairs[0]
           b = two_pairs[1]
           curr_score.append(min(a,b))
           curr_score.append(max(a,b))
       else:
           curr_score.append(1)
           curr_score.append(1)

       three_of_a_kind = self.three_of_a_kind()
       if three_of_a_kind != None:
           curr_score.append(three_of_a_kind)
       else:
           curr_score.append(1)

       straight = self.straight()
       if straight != None:
           curr_score.append(straight)
       else:
           curr_score.append(1)

       flush = self.flush()
       if flush != None:
           curr_score.append(flush)
       else:
           curr_score.append(1)

       fh = self.full_house()
       if fh != None:
           curr_score.append(fh[1])
           curr_score.append(fh[0])
       else:
           curr_score.append(1)
           curr_score.append(1)

       four = self.four_of_a_kind()
       if four != None:
           curr_score.append(four)
       else:
           curr_score.append(1)

       sf = self.straight_flush()
       if sf != None:
           curr_score.append(sf)
       else:
           curr_score.append(1)

       if self.royal_flush():
           curr_score.append(5)
       else:
           curr_score.append(1)

       return curr_score

with open('54.in', 'r') as fp:
    line = fp.readline()
    cnt = 1
    hands1 = []
    hands2 = []
    while line:
        both_cards = line.strip().split(" ")
        cards1 = [Card(c) for c in both_cards[0:5]]
        cards2 = [Card(c) for c in both_cards[5:]]
        hands1.append(Hand(cards1))
        hands2.append(Hand(cards2))

        line = fp.readline()

    cnt = 0
    for i in range(0, len(hands1)):
        a1 = hands1[i].score()
        a2 = hands2[i].score()
        x = len(a1)
        y = len(a2)
        is_large = False
        for i in range(0, x):
            if a1[x - i - 1] > a2[x - i - 1]:
                is_large = True
                break
            elif a1 [x - i - 1] < a2 [ x - i - 1 ]:
                break
        if is_large:
            cnt += 1
    print(cnt)
