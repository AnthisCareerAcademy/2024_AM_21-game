card_value = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
card_suit = ['H', "S", "D","C"]

deck = []

for suit in card_suit:
      for value in card_value:
            x = f"{value}{suit}"
            deck.append(x)

print(deck)