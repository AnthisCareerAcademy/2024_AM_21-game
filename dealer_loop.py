from deck_of_cards import create_deck
from score_checker import check_score

# Below this point is all the new code.
deck_of_cards = create_deck()

# Pop two cards from the deck for the dealer. (This will eventually be
# replaced by the actual code.)
dealer_cards = [deck_of_cards.pop(), deck_of_cards.pop()]

# It's impossible to bust at the start.
dealer_bust = False

# Temporary function to print the cards until we have card art.
def print_cards(cards):
    # Blank message to start.
    message = ""

    # Loop through provided cards.
    for card in cards:
        # Check the value of the card.
        if card[:-1] == "A":
            value = "Ace"
        elif card[:-1] == "J":
            value = "Jack"
        elif card[:-1] == "Q":
            value = "Queen"
        elif card[:-1] == "K":
            value = "King"
        else:
            value = card[:-1]

        # Check the suit of the card.
        if card[-1:] == "S":
            suit = "Spades"
        elif card[-1:] == "D":
            suit = "Diamonds"
        elif card[-1:] == "C":
            suit = "Clubs"
        elif card[-1:] == "H":
            suit = "Heart"
        else:
            suit = "Undefined"

        # Add the value and suit of the cards to the message.
        message += f"\t{value} of {suit}\n"

    # Return the message.
    return message

# Print each card that the dealer has.
print("\nDealer has:")
print(print_cards(dealer_cards))


dealer_score = check_score(dealer_cards)

print(f"\nDealer score is {dealer_score}")

while dealer_score < 17:
    # Here we will deal a card and print the score.
    print("Dealer takes a card...")
    dealer_cards.append(deck_of_cards.pop())

    # Print each card that the dealer has.
    print("\nDealer has:")
    print(print_cards(dealer_cards))

    dealer_score = check_score(dealer_cards)

    print(f"\nDealer score is {dealer_score}")

    if dealer_score > 21:
        dealer_bust = True
        break

if dealer_bust:
    print("\nDealer busted")