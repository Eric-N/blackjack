
import basicstrategy as bs
import game_rules as gr
import hand as h

def complete_player_hand(hand, dealer_up_card, shoe, player, stragegy = bs, rules = gr):

    while hand.complete() is False:

        if len(hand.cards()) == 1: # This can happen after a split
            hand.take_card(shoe.deal_card())

            # if we split aces, we can only take one more card
            if hand.cards()[0] == 1:
                hand.complete(True)
                continue

        if can_split(hand, rules) and should_split(hand, dealer_up_card):
            split(hand, player)
            continue
        
        act = action(hand, dealer_up_card, stragegy)

        if act == 'Dbl':
            if can_double(hand, rules):
                double(hand, shoe)
            else:
                hit(hand, shoe)
        elif act == 'Hit':
            hit(hand, shoe)
        else:
            stand(hand)

def should_split(hand, dealer_up_card, strategy = bs):
    if strategy.split[hand.cards()[0]][dealer_up_card]:
        return True
    else:
        return False

def can_split(hand, rules):
    if hand.cards()[0] != hand.cards()[1]:
        return False
    else:
        return True

def can_double(hand, rules):
    if len(hand.cards()) != 2: # only double if 2 cards
        return False
    
    if hand.did_split():
        if not rules.double_after_split: # no double after split
            return False
    
    return True

def split(hand, player):
    new_hand = h.Hand()

    new_hand.did_split(True)
    hand.did_split(True)

    new_hand.cards().append(hand.cards().pop())
    new_hand_location = player.hands().index(hand) + 1
    player.hands().insert(new_hand_location, new_hand)

def action(hand, dealer_up_card, strategy):
    hand_total = hand.hand_total()
    if hand.soft():
        return strategy.soft[hand_total][dealer_up_card]
    else:
        return strategy.hard[hand_total][dealer_up_card]

def hit(hand, shoe):
    hand.take_card(shoe.deal_card())
    if hand.hand_total() > 21:
        hand.complete(True)

def double(hand, shoe):
    hand.take_card(shoe.deal_card())
    hand.did_double(True)
    hand.complete(True)

def stand(hand):
    hand.complete(True)


