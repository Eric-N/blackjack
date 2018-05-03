import hand as h
import shoe as s
import player as p
import dealer_hand_completer as dhc
import player_hand_completer as phc

shoe = s.Shoe()
shoe.shuffle()

print(shoe.cards())

player_hand = h.Hand()
dealer_hand = h.Hand()

player_hand.take_card(shoe.deal_card())
dealer_hand.take_card(shoe.deal_card())

player_hand.take_card(shoe.deal_card())
dealer_hand.take_card(shoe.deal_card())

player = p.Player()

player.hands(player_hand)

for hand in player.hands():
    phc.complete_player_hand(hand, dealer_hand.cards()[0], shoe, player)

dhc.complete_dealer_hand(dealer_hand, shoe)

print(dealer_hand.cards())

for hand in player.hands():
    print(hand.cards())


# Deal cards
# Check for player and dealer blackjack

# If blackjack .. game is over

# If no blackjacks, finish the player and dealer hands

# If player blackjack and dealer blackjack - push
# If dealer blackjack - dealer win
# If player blackjack - player win
# If payer bust - dealer win
# If dealer bust - player win
# If dealer > player - dealer win
# If player > dealer - player win
# If player = dealer - push