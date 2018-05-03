import hand as h
import shoe as s
import player as p
import dealer_hand_completer as dhc
import player_hand_completer as phc
import game_rules as gr
import numpy as np
import csv

def play(num_games = 1):

    #log_file = open('game_data.txt', 'a')
    log_file = open('game_data.txt', 'a')
    wr = csv.writer(log_file)
    for _ in range(num_games):
        player, dealer_hand, shoe, card_counts = setup()

        #Check for blackjack
        if has_blackjack(dealer_hand) or has_blackjack(player.hands()[0]):
            pass
        else:
            for hand in player.hands():
                phc.complete_player_hand(hand, dealer_hand.cards()[0], shoe, player)
            
            dhc.complete_dealer_hand(dealer_hand, shoe)

        stats = log_results(player, dealer_hand, card_counts)
        #print(stats, file=log_file)
        wr.writerow(stats)
    log_file.close()
    
def log_results(player, dealer_hand, card_counts):

    game_stats = []

    for i in card_counts:
        game_stats.append(card_counts[i])

    factor = win_factor(player, dealer_hand)
    game_stats.append(factor)

    return game_stats

def win_factor(player, dealer_hand):
    factor = 0.0

    for hand in player.hands():
        result = determine_winner(hand, dealer_hand)

        if result == 'win':
            if hand.did_double():
                factor += 2.0
            elif has_blackjack(hand) and (hand.did_split() == False):
                factor += gr.blackjack_payout
            else:
                factor += 1.0
        elif result == 'lose':
            if hand.did_double():
                factor -= 2.0
            else:
                factor -= 1.0
            
    return factor

def determine_winner(hand, dealer_hand):
    result = ''

    player_total = hand.hand_total()
    dealer_total = dealer_hand.hand_total()

    if has_blackjack(dealer_hand) and has_blackjack(hand):
        result = 'push'
    elif has_blackjack(dealer_hand):
        result = 'lose'
    elif has_blackjack(hand):
        result = 'win'
    elif player_total > 21:
        result = 'lose'
    elif dealer_total > 21:
        result = 'win'
    elif dealer_total > player_total:
        result = 'lose'
    elif player_total > dealer_total:
        result = 'win'
    else:
        result = 'push'

    return result

def setup():
    shoe = s.Shoe(numdecks = 6)
    shoe.shuffle()

    del shoe.cards()[:150]

    a = np.array(shoe.cards())
    unique, counts = np.unique(a, return_counts=True)
    card_counts = dict(zip(unique, counts))

    player_hand = h.Hand()
    dealer_hand = h.Hand()

    player_hand.take_card(shoe.deal_card())
    dealer_hand.take_card(shoe.deal_card())

    player_hand.take_card(shoe.deal_card())
    dealer_hand.take_card(shoe.deal_card())

    player = p.Player()

    player.hands(player_hand)

    return (player, dealer_hand, shoe, card_counts)

def has_blackjack(hand):
    if len(hand.cards()) == 2 and hand.hand_total() == 21:
        hand.has_blackjack(True)
        return True


if __name__ == '__main__':
        play(num_games = 1000000)