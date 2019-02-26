#!/usr/bin/env python
from carddeck import CardDeck

class Dog():
    def bark(self):
        print("Woof! Woof!")

class JokerDeck(Dog, CardDeck):

    def _create_deck(self):
        super()._create_deck()
        self._cards.append(('Joker', 1))
        self._cards.append(('Joker', 2))
