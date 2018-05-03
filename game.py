import shoe as s
import hand as h
import basicstrategy

class Game:
    def __init__(self):
        self._player_hands = [h.Hand()]
        self._dealer_hand = h.Hand()
        self._shoe = s.Shoe()
        self._complete = False

    def player_hands(self):
        return self._player_hands
    
    def dealer_hand(self):
        return self._dealer_hand

    def set_up(self):
        self._shoe.shuffle()

        self._player_hands[0].take_card(self._shoe.deal_card())
        self._dealer_hand.take_card(self._shoe.deal_card())

        self._player_hands[0].take_card(self._shoe.deal_card())
        self._dealer_hand.take_card(self._shoe.deal_card())

    def play(self):
        self.set_up()

        # Check for dealer blackjack
        if self.dealer_hand().hand_total() == 21:
            self.print_results()
            return

        # We have to check for player blackjack too
        # If player has blackjack, player wins at the beginning
        # Even if the dealer eventually draws to a 21

        # There may be multiple hands as a result of splits.
        # So, for hand in hands
        # Complete Player hand
        for x in self.player_hands():
            self.complete_player_hand(x)

        # Complete Dealer Hand
        self.complete_dealer_hand(self.dealer_hand())

        # Print Out Results
        self.print_results()
    
    def print_results(self):
        print('Number of player hands: {}'.format(len(self._player_hands)))

        for x in self.player_hands():
            print('{} - {}'.format(x.cards(), x.hand_total()))
            print('{} - {}'.format(self.dealer_hand().cards(), self.dealer_hand().hand_total()))

            # Player Bust
            if x.hand_total() > 21:
                print('Player Bust! Player Looses')
            elif self.dealer_hand().hand_total() > 21:
                print('Dealer Bust! Plaer Wins!')
            elif x.hand_total() > self.dealer_hand().hand_total():
                print('Player Wins!')
            elif x.hand_total() < self.dealer_hand().hand_total():
                print('Player Looses')
            else:
                print('It\'s a tie!')



    def complete_player_hand(self, htc):

        # If only one card in hand, take another card
        # This happens as a result of a split
        if len(htc.cards()) == 1:
            htc.take_card(self._shoe.deal_card())

        # while hand is not complete
        while htc.complete() == False:
            # must call hand_total() to get correct hard or soft
            player_total = htc.hand_total()

            if player_total > 21:
                htc.complete(True)
                continue
            
            dealer_up_card = self.dealer_hand().cards()[0]

            #Split
            if len(htc.cards()) == 2 and htc.cards()[0] == htc.cards()[1]:
                if basicstrategy.split[htc.cards()[0]][dealer_up_card]:
                    # split
                    # create a new hand
                    new_hand = h.Hand()
                    # move [1] from current hand to new hand
                    new_hand.take_card(htc.cards().pop())
                    # append new hand to hands
                    self.player_hands().append(new_hand)
                    continue

            # Choose our move
            if htc.soft() == False:
                action = basicstrategy.hard[player_total][dealer_up_card]
            else:
                action = basicstrategy.soft[player_total][dealer_up_card]

            # If Stand - make hand complete and continue
            if action == "Dbl":
                htc.take_card(self._shoe.deal_card())
                htc.complete(True)
                continue
            elif action == "Hit":
                htc.take_card(self._shoe.deal_card())
                continue
            else:
                htc.complete(True)
                continue

    def complete_dealer_hand(self, htc):
        dealer_total = htc.hand_total()

        # take into considerateion hit on soft 17
        while dealer_total < 17:
            htc.take_card(self._shoe.deal_card())
            dealer_total = htc.hand_total()
