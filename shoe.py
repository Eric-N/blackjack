import timeit
import numpy as np

class Shoe:
    def __init__(self, numdecks = 1):
        self._cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4*numdecks

    def cards(self):
        return self._cards

    def shuffle(self):
        np.random.shuffle(self._cards)

    def deal_card(self):
        return self._cards.pop()
        

def test(numdecks = 6, numshuffles = 1000000):
    print('Shuffling a {} deck shoe {:,} times:'.format(numdecks, numshuffles))
    s = 'from __main__ import Shoe; shoe = Shoe({})'.format(numdecks)
    print(timeit.timeit('shoe.shuffle()', number = numshuffles, setup = s))


if __name__ == '__main__':
    test()