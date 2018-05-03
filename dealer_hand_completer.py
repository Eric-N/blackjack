import game_rules as gr

def complete_dealer_hand(dealer_hand, shoe, game_rules = gr):

    while dealer_hand.complete() == False:
        dealer_total = dealer_hand.hand_total()

        if dealer_total == 17:
            if dealer_hand.soft() == True:
                if game_rules.dealer_hits_soft_17:
                    dealer_hand.take_card(shoe.deal_card())
                    continue
            else:
                dealer_hand.complete(True)
                continue

        if dealer_total < 17:
            dealer_hand.take_card(shoe.deal_card())
        else:
            dealer_hand.complete(True)