# https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/238.py

from random import shuffle


def generate_random_card_sequence():
    cards = [i for _ in range(4) for i in range(1, 11)]
    shuffle(cards)
    return cards


def get_best_player_score(
    sequence, player_score: int = 0, dealer_score: int = 0
):
    if not sequence:
        return player_score, dealer_score
    elif player_score > 21 and dealer_score > 21:
        return -1, -1
    elif player_score > 21:
        return -1, dealer_score
    elif dealer_score > 21:
        return player_score, -1
    return max(
        get_best_player_score(sequence[1:], player_score + sequence[0], dealer_score),
        get_best_player_score(sequence[1:], player_score, dealer_score + sequence[0]),
        (player_score, dealer_score),
        # the player's score has more weightage than the dealer's score
        key=lambda x: 1.01 * x[0] + x[1],
    )


def simulate(n: int = 1_000) -> float:
    # simulating the game n times and returning the percent of victories for the player
    wins = 0
    for _ in range(n):
        sequence = generate_random_card_sequence()
        player_score, dealer_score = get_best_player_score(sequence)
        if player_score > dealer_score and player_score <= 21:
            wins += 1
    return (wins / n) * 100


if __name__ == "__main__":
    print(f"The Player won {simulate():.2f}% of the times")