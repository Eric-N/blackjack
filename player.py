class Player():
    def __init__(self):
        self._hands = []

    def hands(self, hand = None):
        if hand: self._hands.append(hand)
        return self._hands