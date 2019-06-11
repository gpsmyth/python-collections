suits = ('hearts', 'diamonds', 'clubs', 'spades' )
values = range(1,14)
list(values)
cards = []
for s in suits:
    for v in values:
        cards.append("{0} of {1}".format(v,s))
print (cards)
import random
random.choice(cards)
random.shuffle(cards)
cards
print (random.choice(cards))
