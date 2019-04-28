""" TODO optimise
Swap out costly list insert and pops with a deque.
Takes a million years to run pt 2 otherwise.
"""

from itertools import cycle


def pt_1(players=7, last_marble=25):
    # py3.7 ordered guaranteed
    players = range(1, players + 1)
    scores = {player: 0 for player in players}
    marbles = [0]
    current_marble_index = 0

    for marble, player in zip(range(1, last_marble + 1), cycle(players)):
        if marble % 23 == 0:
            # Remove from circle & add to score
            pop_index = (current_marble_index - 7) % len(marbles)

            # Add score to player
            score_earned = marble + marbles.pop(pop_index)
            scores[player] += score_earned

            # Marble to the right is now current marble
            current_marble_index = pop_index
        else:
            insert_index = (current_marble_index + 2) % len(marbles)
            # Append to list instead of begginning
            if not insert_index:
                insert_index = len(marbles)
            marbles.insert(insert_index, marble)
            current_marble_index = insert_index
    return max(scores.values())


if __name__ == "__main__":
    # Tests
    assert pt_1(7, 25) == 32
    assert pt_1(10, 1618) == 8317
    assert pt_1(13, 7999) == 146373
    assert pt_1(17, 1104) == 2764
    assert pt_1(30, 5807) == 37305

    # pt1
    print(pt_1(419, 71052))
    # pt 2
    print(pt_1(419, 71052 * 100))
