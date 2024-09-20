def check_score(cards):
    score = 0

    # These cards have special point values.
    special_cases = ["J", "Q", "K", "A"]

    for card in cards:
        # If the card is not a special card (face, ace), add its points.
        if card[:-1] not in special_cases:
            score += int(card[:-1])
        else:
            # If the card is an ace, and 11 points can safely be added, then
            # add 11 points.
            if card[:-1] == "A" and score + 11 <= 21:
                score += 11
            # If 11 points cannot be added, then add 1 point.
            elif card[:-1] == "A" and score + 11 > 21:
                score += 1
            # Otherwise, if it's a face card, add 10 points.
            else:
                score += 10

    # Return the score of the cards.
    return score

print(check_score(["KH", "2S", "AD"]))