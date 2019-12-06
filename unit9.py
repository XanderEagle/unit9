import card
import deck


def my_dealer(my_deck):
    cards_deal = []
    for x in range(5):
        cards_deal.append(my_deck.deal())
    return cards_deal


def compare_cards(player1, player2):
    if player1 > player2:
        return "Player 1"
    else:
        return "Player 2"


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player1 = my_dealer(my_deck)
    player2 = my_dealer(my_deck)
    for x in range(5):
        print(compare_cards(player1[x], player2[x]))


main()
