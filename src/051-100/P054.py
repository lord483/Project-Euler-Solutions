'''
    Problem 54 - Poker hands - WIP
'''
from collections import Counter

value = {
    "A": 14,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}


class hand:
    def __init__(self, deck):
        self.deck = self.sorted_deck(deck)
        self.high_card = self.deck[-1][0]
        self.flush, self.straight_flush, self.royal_flush = self.check_flush()
        self.four = self.check_four()
        self.one_pair, self.two_pair, self.three, self.full_house = self.check_full_house(
        )
        self.straight = self.check_straight()

    def sorted_deck(self, deck):
        d = [(value[card[0]], card[1]) for card in deck]
        d.sort(key=lambda x: x[0])
        return d

    def check_flush(self):
        f, sf, rf = 0, 0, 0

        if len(set([x[1] for x in self.deck])) == 1:
            f = 1
            values = [v for v, s in self.deck]
            values.sort()
            first = values[0]
            last = values[-1]
            if last == first + 4:
                sf = first
                if first == 10:
                    rf = 1

        return f, sf, rf

    def check_four(self):
        four = 0
        values = [x[0] for x in self.deck]
        if values[0] == values[3]:
            four = values[0]
        elif values[1] == values[-1]:
            four = values[1]
        return four

    def check_full_house(self):
        one_pair, two_pair, three, full = 0, 0, 0, 0
        values = [x[0] for x in self.deck]
        c = Counter(values)
        c_p = [(k, c[k]) for k in c.keys()]
        c_p.sort(key=lambda x: x[0], reverse=True)
        c_p.sort(key=lambda x: x[1], reverse=True)

        if c_p[0][1] == 3:
            three = c_p[0][0]
            if c_p[1][1] == 2:
                one_pair = c_p[1][0]
                full = 1

        if c_p[0][1] == 2:
            one_pair = c_p[0][0]
            if c_p[1][1] == 2:
                two_pair = c_p[1][0]

        return one_pair, two_pair, three, full

    def check_straight(self):
        s = 0
        values = [x[0] for x in self.deck]
        if len(set(values)) == 5:
            if values[-1] == values[0] + 4:
                return values[0]
        return s


def winner(a, b):
    '''
        return 1 if A (Player1) is winning else 0
    '''
    winner = -1

    A = hand(a)
    B = hand(b)

    if A.royal_flush > B.royal_flush:
        return 1
    elif B.royal_flush > A.royal_flush:
        return 0

    if A.straight_flush > B.straight_flush:
        return 1
    elif B.straight_flush > A.straight_flush:
        return 0

    if A.four > B.four:
        return 1
    elif B.four > A.four:
        return 0

    if A.full_house > B.full_house:
        return 1
    elif B.full_house > A.full_house:
        return 0

    if A.flush > B.flush:
        return 1
    elif B.flush > A.flush:
        return 0

    if A.straight > B.straight:
        return 1
    elif B.straight > A.straight:
        return 0

    if A.three > B.three:
        return 1
    elif B.three > A.three:
        return 0

    if A.two_pair > B.two_pair:
        return 1
    elif B.two_pair > A.two_pair:
        return 0

    if A.one_pair > B.one_pair:
        return 1
    elif B.one_pair > A.one_pair:
        return 0

    if A.high_card > B.high_card:
        return 1
    elif B.high_card > A.high_card:
        return 0

    print("No winner : ", a, b)

    return winner


if __name__ == "__main__":
    res = 0
    with open("p054_poker.txt") as f:
        for line in f:
            cards = list(line.strip().split())
            a, b = cards[:5], cards[5:]
            w = winner(a, b)
            # print(a, b, w)
            res += w
    print(res)
