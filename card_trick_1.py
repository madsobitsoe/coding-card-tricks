#!/bin/env/python
import random

# The Trick
# Two piles of 15 cards
# "Magician" has jack of hearts. "uses" it to find players card
# Player selects a card from the remaining 21. "Magician doesn't see"
# Player splits one pile of cards into two piles at random.
# Magician splits the other pile into two piles at random
# Player puts selected card on top of one of the original stacks.
# "Magician" puts JoH picture side up, on top of the other original stack.
# The cards that were lifted off of each stack are put on the opposite
# original stack.
#
# "Magicians" stack is put on top of the players stack
# Magician starts sorting cards into two piles
# every odd card in one, every even in the other.
# The stack containing the jack is kept, the other is discarded.
# This continues until a stack with just JoH and another card is left.
# This will be the players card.

# Trick works because the lift-off is put on the other stack.
# This aligns the indexes of JoH and the players card,
# leaving n/2 cards between them, where n is the stacksize,
# as well as leaving both cards either odd or even indexed.
# Then by sorting into two stacks and selecting the stack with JoH,
# knowing that this stack contains the players card,
# the players card will be found. Trick works with
# initial stacksizes of (2^n) - 1, yielding a total amount of cards
# in the trick to be 2^n+1, given the deck is made larger
# and JoH and players_card duplicates are removed
# before finding the card (in this version, not in real life).


def create_piles(size):
    for i in range((2 << size - 1) - 1):
        pile11.append(deck.pop(random.randrange(len(deck))))
    for i in range((2 << size - 1) - 1):
        pile21.append(deck.pop(random.randrange(len(deck))))

def print_card(card, players_card, joh):
    if card == players_card:
        return 'P '
    elif card == joh:
        return 'J '
    else:
        return '. '


def print_stack(stack, players_card, jack_of_hearts):
    print ''.join(
        map(lambda x: print_card(x,
                                 players_card,
                                 jack_of_hearts),
            stack))


if __name__ == '__main__':
    # Set decksize 2^n
    intial_stack_size_2n = 8
    # Generate a deck of cards
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    deck = []
    while len(deck) < (2 << (intial_stack_size_2n)):
        deck += [(i, suit) for i in range(1, 14) for suit in suits]

    print "Size of deck: %d" % len(deck)

    # We have four piles of cards.
    # two with 15 cards each and two empty
    pile11 = []
    pile12 = []
    pile21 = []
    pile22 = []

    jack_of_hearts = (11, 'hearts')

    while jack_of_hearts in deck:
        deck.remove(jack_of_hearts)

    players_card = deck.pop(random.randrange(len(deck)))
    while players_card in deck:
        deck.remove(players_card)

    # create two piles of size 2 << 2n-1
    create_piles(intial_stack_size_2n - 1)
    print "Players card: %s" % (players_card,)
    print "Jack of hearts: %s" % (jack_of_hearts,)

    n = random.randint(0, len(pile11)-2)
    pile12 = pile11[n:]
    pile11 = pile11[:n]

    n = random.randint(0, len(pile21)-2)
    pile22 = pile21[n:]
    pile21 = pile21[:n]

    # Select a pile to put players card on
    # and put card there. Put JoH on other pile
    if random.randint(0, 1) == 0:
        pile11.append(players_card)
        pile21.append(jack_of_hearts)
    else:        
        pile21.append(players_card)
        pile11.append(jack_of_hearts)
    pile11 += pile22
    pile21 += pile12

    # Join the stacks in one big sorting stack
    final_stack = pile11 + pile21
    print "Final stack has %d cards" % len(final_stack)

    # throw half of the cards away until we find the players card
    while (len(final_stack) > 2):
        print "Both cards are in stack: %r" % (
            players_card in final_stack and
            jack_of_hearts in final_stack)
        print "Index of P: %d\nIndex of J: %d" % (
            final_stack.index(players_card),
            final_stack.index(jack_of_hearts))

        print_stack(final_stack, players_card, jack_of_hearts)

        index = final_stack.index(jack_of_hearts)
        players_index = final_stack.index(players_card)

        final_stack = [final_stack[i] for i in range(
            len(final_stack)) if i % 2 == index % 2]

    print_stack(final_stack, players_card, jack_of_hearts)

    print "Players card should be: %s" % (players_card,)
    final_stack.remove(jack_of_hearts)
    print "Found card is: %s" % ((final_stack[0],))
