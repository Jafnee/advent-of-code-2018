from collections import Counter


with open('day02-input.txt', 'r') as input_file:
    ids = [id.strip() for id in input_file]

# For each ID count the number of times each character is found.
repeats_counters = (Counter(id).values() for id in ids)

double_occurrences = 0
triple_occurrences = 0
for repeats_counter in repeats_counters:
    if 2 in repeats_counter:
        double_occurrences += 1
    if 3 in repeats_counter:
        triple_occurrences += 1

# pt 1
print(double_occurrences * triple_occurrences)

for index, id in enumerate(ids):
    # Only compare against IDs after the current.
    ids_to_compare = ids[index + 1:]
    for other_id in ids_to_compare:
        # Find characters that are different, in the same position.
        diffs = [i for i in range(len(id)) if id[i] != other_id[i]]
        if len(diffs) == 1:
            diff_index = diffs[0]
            # pt 2
            # Rebuild string without the different character
            print(id[:diff_index] + id[diff_index + 1:])
            break

