# get_metadata
def pt1(tree, meta_data=[]):
    children_header, metadata_header, *tree = tree
    for n in range(children_header):
        tree, meta_data = pt1(tree, meta_data)
    meta_data += tree[:metadata_header]

    remaining = tree[metadata_header:]
    if remaining:
        return remaining, meta_data
    return meta_data

def pt2(tree):
    # TODO
    pass


if __name__ == "__main__":
    with open('day08-input.txt') as input_file:
        tree = [int(x) for x in input_file.readline().split()]
    # pt 1
    print(sum(pt1(tree)))
    # pt 2
    print(pt2(tree))
