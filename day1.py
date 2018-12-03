from itertools import cycle


with open('day1-input.txt', 'r') as input_file:
    numbers = [int(num) for num in input_file]
# pt 1
print(sum(numbers))

occurred_frequencies = {0}
current = 0
for number in cycle(numbers):
    current += number
    already_occured = current in occurred_frequencies
    if already_occured:
        # pt 2
        print(current)
        break
    occurred_frequencies.add(current)

