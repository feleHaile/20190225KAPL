#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Bob')

print(d1.get_dealer())

print(d1.dealer)

d1.dealer = 'Lamont'

print(d1.dealer)

d1.shuffle()

print(d1.cards)

print(d1.get_suits())
print(CardDeck.get_suits())

print(d1)

print(len(d1))
d2 = CardDeck("Julius")

d3 = d1 + d2
print(d3, len(d3))
print()
j1 = JokerDeck("Albert")
j1.shuffle()
print(j1.cards)
j1.bark()
