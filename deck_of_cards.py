import random

def create_deck():
      deck = []
      card_value = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
      card_suit = ['H', "S", "D","C"]
      for suit in card_suit:
            for value in card_value:
                  x = f"{value}{suit}"
                  deck.append(x)
      random.shuffle(deck)
      #print(deck)
      
      return deck


      


new_deck = create_deck()

print(new_deck)