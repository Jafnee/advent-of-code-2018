from itertools import cycle
from collections import deque


def pt_1(players=7, last_marble=25):
    # py3.7 ordered guaranteed
    players = range(1, players + 1)
    scores = {player: 0 for player in players}
    marbles = deque([0])

    for marble, player in zip(range(1, last_marble + 1), cycle(players)):
        if marble % 23 == 0:
            # Remove from circle & add to score
            marbles.rotate(-7)
            scores[player] += marble + marbles.pop()
        else:
            marbles.rotate(2)
            marbles.append(marble)
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
