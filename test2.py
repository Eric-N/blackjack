import hand as h
import shoe as s
import dealer_hand_completer as dhc

shoe = s.Shoe()
shoe.shuffle()

dealer_hand = h.Hand()

dealer_hand.take_card(shoe.deal_card())
dealer_hand.take_card(shoe.deal_card())

dhc.complete_dealer_hand(dealer_hand, shoe)

print(dealer_hand.cards())