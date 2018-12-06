from collections import defaultdict, Counter


def get_manhattan(x, y, x_goal, y_goal):
    return abs(x - x_goal) + abs(y - y_goal)


def get_edges(coords):
    top = float('inf')
    bottom = 0
    right = 0
    left = float('inf')
    for coord in coords:
        top = min(top, coord[1])
        bottom = max(bottom, coord[1])
        right = max(right, coord[0])
        left = min(left, coord[0])
    return top, right, bottom, left


def make_on_edge(top, right, bottom, left):
    def on_edge(x, y):
        result = x in [right, left] or y in [top, bottom]
        return result
    return on_edge


def make_get_closest_coord(coords):
    def get_closest_coord(x, y):
        distances = defaultdict(list)
        for coord in coords:
            distances[get_manhattan(x, y, *coord)].append(coord)
        closest_distance = min(distances.keys())
        # Got clash
        if len(distances[closest_distance]) > 1:
            return None
        return distances[closest_distance][0]
    return get_closest_coord


def make_get_distance_sum(coords):
    def get_distance_sum(x, y):
        return sum(get_manhattan(x, y, *coord) for coord in coords)
    return get_distance_sum


if __name__ == '__main__':
    with open('day06-input.txt', 'r') as input_file:
        coords = [
            tuple(int(x) for x in line.strip().split(', '))
            for line
            in input_file
        ]
    top, right, bottom, left = get_edges(coords)
    is_infinite = make_on_edge(top, right, bottom, left)
    # Remove infinite coords
    get_closest_coord = make_get_closest_coord(coords)
    get_distance_sum = make_get_distance_sum(coords)
    areas_owned = defaultdict(int)
    infinite_coords = set()

    coordinates_close_to_all = 0

    for x in range(left, right + 1):
        for y in range(top, bottom + 1):
            if get_distance_sum(x, y) < 10000:
                coordinates_close_to_all += 1
            closest_coord = get_closest_coord(x, y)
            # Got clash
            if closest_coord is None:
                continue
            if is_infinite(x, y):
                infinite_coords.add(closest_coord)
            areas_owned[closest_coord] += 1
    non_infinite_coords = dict(
        coord
        for coord
        in areas_owned.items()
        if coord[0] not in infinite_coords
    )
    # pt 1
    print(Counter(non_infinite_coords).most_common()[0][1])
    # pt 2
    print(coordinates_close_to_all)
