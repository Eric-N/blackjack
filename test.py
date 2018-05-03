import shoe as s
import hand as h
import player as p
import player_hand_completer as phc

shoe = s.Shoe()
shoe.shuffle()

player = p.Player()

player_hand = h.Hand()
player_hand.take_cards(1,1)
#player_hand.take_card(shoe.deal_card())
#player_hand.take_card(shoe.deal_card())

player.hands(player_hand)

dealer_hand = h.Hand()
dealer_hand.take_card(shoe.deal_card())
dealer_hand.take_card(shoe.deal_card())

dealer_up_card = dealer_hand.cards()[0]
print(dealer_up_card)

for hand in player.hands():
    phc.complete_player_hand(hand, dealer_up_card, shoe, player)

for hand in player.hands():
    print(hand.cards())




