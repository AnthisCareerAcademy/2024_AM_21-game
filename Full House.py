dice_1 = 1
dice_2 = 1
dice_3 = 6
dice_4 = 6
dice_5 = 6

from collections import Counter

dice_list = [dice_1, dice_2, dice_3, dice_4, dice_5]
count = Counter(dice_list)

sort_dice = {}
for dice, frequency in count.items():
    sort_dice[dice] = frequency

print(sort_dice)


value_2 = 2
value_3 = 3

if value_2 in sort_dice.values():
    if value_3 in sort_dice.values():
        full_house = True
    else:
        full_house = False
else:
    full_house = False

if full_house == True:
    print("You earned 25 points")
else:
    print("You can't do a full house")