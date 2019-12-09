# by Xander Eagle
# December 9, 2019
# Card Game of Compare (War)

import deck


def my_dealer(my_deck):
    """
        :param my_deck: import the class of deck
        :return: the cards dealt
        """
    cards_deal = []
    for x in range(5):
        cards_deal.append(my_deck.deal())
    return cards_deal


def compare_cards(player1, player2):
    """
        :param player1: Player1's cards
        :param player2: Player2's cards
        :return: who wins
        """
    if player1 > player2:
        return "Player1"
    else:
        return "Player2"


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player1 = (my_dealer(my_deck))
    player2 = (my_dealer(my_deck))
    score = 0
    score2 = 0
    for x in range(5):
        print(compare_cards(player1[x], player2[x]))
        if player1[x] > player2[x]:
            score = score + 1
        else:
            score2 = score2 + 1
    print("Player1 won", score, "times")
    print("Player2 won", score2, "times")
    if score > score2:
        print("  Player1 won the Game of Compare!")
    else:
        print("  Player2 won the Game of Compare!")


main()
