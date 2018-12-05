def fully_react_polymer(polymer):
    polymer = list(polymer)
    start_index = 0
    while True:
        for index in range(start_index, len(polymer)):
            unit1 = polymer[index]
            try:
                unit2 = polymer[index + 1]
            except IndexError:
                # reached the end
                pass
            if unit1.lower() == unit2.lower() and unit1 != unit2:
                del polymer[index:index + 2]
                # Restart from just before this reaction.
                start_index = 0 if index == 0 else index - 1
                break
        else:
            return polymer


def shortest_length_by_removing(polymer):
    # pypy 5.10 doesn't have math.inf
    shortest = float('inf')
    for unit in set(polymer.lower()):
        removed_polymer = polymer.replace(unit.upper(), '').replace(unit.lower(), '')
        reacted_polymer_length = len(fully_react_polymer(removed_polymer))
        shortest = reacted_polymer_length if reacted_polymer_length < shortest else shortest
    return shortest



if __name__ == '__main__':
    with open('day05-input.txt', 'r') as input_file:
        polymer = input_file.readline().strip()
        reacted_polymer = fully_react_polymer(polymer)
        # pt 1
        print(len(reacted_polymer))
        # pt 2
        print(shortest_length_by_removing(polymer))
