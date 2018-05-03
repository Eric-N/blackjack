import numpy as np

class Hand:
    def __init__(self):
        self._cards = []
        self._soft = False
        self._complete = False
        self._did_split = False
        self._did_double = False
        self._has_blackjack = False

    def has_blackjack(self, b = None):
        if b: self._had_blackjack = True
        return self._has_blackjack

    def did_double(self, d = None):
        if d: self._did_double = d
        return self._did_double

    def did_split(self, s = None):
        if s: self._did_split = s
        return self._did_split

    def cards(self):
        return self._cards

    def soft(self):
        # self.hand_total() # soft is only correct after calculating hand total
        return self._soft
        
    def complete(self, c = None):
        if c: self._complete = c
        return self._complete
    
    def take_card(self, card):
        self._cards.append(card)

    def take_cards(self, *args):
        for c in args:
            self._cards.append(c)
    
    def hand_total(self):
        sum = 0

        soft = False
        for c in self._cards:
            if c == 1 and soft == False:
                sum += 11
                self._soft = True
                soft = True
            else:
                sum += c
        
        if sum > 21 and soft == True:
            sum -= 10
            self._soft = False
            soft = False
        
        return sum