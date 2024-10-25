from collections import Counter
def full_house(DiceList):
    count = Counter(DiceList)

    sort_dice = {}
    for dice, frequency in count.items():
        sort_dice[dice] = frequency

    print(sort_dice)

    value_2 = 2
    value_3 = 3

    if value_2 in sort_dice.values():
        if value_3 in sort_dice.values():
            fullhouse = True
        else:
            fullhouse = False
    else:
        fullhouse = False

    if fullhouse == True:
        print("You earned 25 points")
    else:
        print("You can't do a full house")