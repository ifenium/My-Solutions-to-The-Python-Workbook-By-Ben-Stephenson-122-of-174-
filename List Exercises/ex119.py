'''
Exercise 119: Dealing Hands of Cards
In many card games each player is dealt a specific number of cards after the deck
has been shuffled. Write a function, deal, which takes the number of hands, the
number of cards per hand, and a deck of cards as its three parameters. Your function
should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards.
When dealing the hands, your function should modify the deck of cards passed
to it as a parameter, removing each card from the deck as it is added to a player’s
hand. When cards are dealt, it is customary to give each player a card before any
player receives an additional card. Your function should follow this custom when
constructing the hands for the players.
Use your solution to Exercise 118 to help you construct a main program that
creates and shuffles a deck of cards, and then deals out four hands of five cards each.
Display all of the hands of cards, along with the cards remaining in the deck after
the hands have been dealt.
'''

from random import randrange

def createDeck():
    cards = []
    
    for suit in ['c','d','h','s']:
        for value in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
            cards.append(value + suit)
    return cards

def shuffle(cards):
    for i in range(0, len(cards)):
        pos = randrange(0, len(cards))
        temp  = cards[i]
        cards[i] = cards[pos]
        cards[pos] = temp

def deal(hands, cards_per_hand, cards):
    deals = []
     
    for i in range(hands):
        for j in range(cards_per_hand):
            current = []
            current.append(cards)
        deals.append(current)

    print(deals)

def main():
    cards = createDeck()
    cards = shuffle(cards)
    deal(4, 5, cards)

if __name__ == '__main__':
    main()