'''
Game Loop:
Check is action == 'stand' or 'hit'
if 'hit', deal another card
if 'stand', check if they won the game
if 'bust' or 'lose', end game with lose statement
'''
from deck_of_cards import new_deck
from score_checker import check_score

dealer_score=0

def player_hand():
    print(f"Player Hand: {player_cards}")

def deal_player():
    card1 = new_deck
    new_deck.remove(card1)
    card2 = new_deck
    new_deck.remove(card2)

# Initialize the player hand.
player_cards = [new_deck.pop(), new_deck.pop()]

# Display the player score.
player_hand()
player_score = check_score(player_cards)
print(f"Player's score is {player_score}")

action = ""
while action != "stand":

    action = input("Would you like to 'hit' or 'stand'? ")

    # If the player hits, give them a new card.
    if action.lower() == 'hit':
        player_cards.append(new_deck.pop())
        player_hand()

        # Check if the player has busted
        player_score = check_score(player_cards)
        print(f"Player's score is {player_score}")

        if player_score > 21:
            print("You busted!")
            break





