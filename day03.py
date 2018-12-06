import re
import csv
from collections import Counter


CLAIM_PATTERN = re.compile(r'^#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<width>\d+)x(?P<height>\d+)')
COLLISION_CHAR = 'X'
FABRIC_SIZE = 1000


def claim_parser(claim):
    match = re.match(CLAIM_PATTERN, claim)
    return tuple(int(x) for x in match.groups())


with open('day03-input.txt', 'r') as input_file:
    claims = [claim_parser(row.strip()) for row in input_file]

# Init fabric
fabric = [[''] * FABRIC_SIZE for _ in range(FABRIC_SIZE)]

collisions = 0

for claim in claims:
    id, x, y, width, height = claim

    for i in range(width):
        for j in range(height):
            current_x = x + i
            current_y = y + j
            existing_value = fabric[current_y][current_x]
            insert_value = id
            if existing_value:
                if existing_value in [id, COLLISION_CHAR]:
                    continue
                # Fresh collision
                collisions += 1
                insert_value = COLLISION_CHAR
            fabric[current_y][current_x] = insert_value

# pt 1
print(collisions)

# Lazy style 😬
# Just do the same thing again to find the one that doesn't overlap.
for claim in claims:
    id, x, y, width, height = claim
    collided = False

    for i in range(width):
        for j in range(height):
            existing_value = fabric[y + j][x + i]
            if existing_value and existing_value != id:
                collided = True
                continue
    if not collided:
        # pt 2
        print(id)
        # Only 1 claim doesn't collide.
        break

# Visuallize the fabric in a spreadsheet
with open('day03-fabric.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(fabric)
