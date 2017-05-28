# coding-card-tricks
Implementing simple card tricks in python to figure out how they work.

## The trick card_trick_1.py

- Two piles of (2^n)-1 cards. Use 15 if done with a physical deck of cards.

1. "Magician" has jack of hearts and "uses" it to find players card.
2. Player selects a card from the remaining 21. "Magician doesn't see"
3. Player splits one pile of cards into two piles at random.
4. Magician splits the other pile into two piles at random
5. Player puts selected card on top of one of the original stacks.
6. "Magician" puts JoH picture side up, on top of the other original stack.
7. The cards that were lifted off of each stack are put on the opposite
original stack.
8. "Magicians" stack is put on top of the players stack
9. Magician starts sorting cards into two piles
every odd card in one, every even in the other.
10. The stack containing the jack is kept, the other is discarded.
11. This continues until a stack with just JoH and another card is left.
This will be the players card.


## Explanation
Trick works because the lift-off is put on the other stack.  
This aligns the indexes of JoH and the players card,
leaving **n/2** cards between them, where **n** is the stacksize,  
as well as leaving both cards either odd or even indexed.  
Then by sorting into two stacks and selecting the stack with JoH,  
knowing that this stack contains the players card,  
the players card will be found. 

Trick works with initial stacksizes of (2^n) - 1,  
yielding a total amount of cards in the trick to be 2^n+1,  
given the deck is made larger and JoH and players_card duplicates  
are removed before finding the card (in this version, not in real life).  
