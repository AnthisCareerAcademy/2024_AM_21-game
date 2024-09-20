if dealer_score == 21:
    if player_score == 21:
        print(tie)
    else:
        print(lose)
else:
    if player_score > 21:
        print(lose)
    else:

        # insert the game loop
        # insert the dealer loop

        if dealer_score > 21:
            print(win)
        elif player_score > dealer_score:
            print(win)
        elif player_score == dealer_score:
            print(tie)
        elif player_score < dealer_score:
            print(lose)
