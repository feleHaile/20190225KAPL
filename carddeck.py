#!/usr/bin/env python
import random


class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):  # constructor
        self._cards = None
        self.dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards


    # getter method
    def get_dealer(self):
        return self._dealer

    # setter method
    def set_dealer(self, dealer):
        self._dealer = dealer

    # getter property
    @property  # generic
    def dealer(self):
        return self._dealer

    # dealer = property(dealer)

    # setter property
    @dealer.setter  # specific
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        name = type(self).__name__
        return "{}({})".format(name, len(self))

    def __add__(self, other):  # implement '+' operator
        tmp = CardDeck(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp

    # option 1: getter method
    # option 2: getter property
    #    foo.get_dealer()  method function
    #    foo.dealer        property function

if __name__ == '__main__':
    d1 = CardDeck("Joe")
    d2 = CardDeck("Mary")
    d3 = CardDeck("Priscilla")
    print(d1.get_suits())

