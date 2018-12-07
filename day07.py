import re
from collections import defaultdict


INSTRUCTION_PATTERN = re.compile(r'^Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
def parse_instruction(instruction):
    match = re.search(INSTRUCTION_PATTERN, instruction)
    return match.groups()


def remove_prereq(graph, step):
    return {
        key: set(value for value in value if value != step)
        for key, value
        in graph.items()
    }


def get_graph(instructions):
    # step: [prerequisite steps]
    graph = defaultdict(set)
    for i in instructions:
        pre, step = parse_instruction(i)
        # Ensure key exists for steps without prereqs
        graph[pre].update()
        graph[step].add(pre)
    return graph


def pt1(instructions):
    graph = get_graph(instructions)

    order = []
    while True:
        # Add first (alphabetically) available task.
        for step in sorted(graph):
            if not graph[step]:
                order.append(step)
                # Step is done, remove it from other steps prereqs
                graph = remove_prereq(graph, step)
                del graph[step]
                break
        # graph exhausted
        else:
            break
    return "".join(order)


WORKERS = 5
BASE_MINUTES = 60
def pt2(instructions):
    graph = get_graph(instructions)
    seconds_required = dict(
        (step, mins)
        for mins, step
        in enumerate(sorted(graph.keys()), BASE_MINUTES + 1)
    )
    working_on = {}
    seconds = 0
    while True:
        available_steps = [
            step for step
            in sorted(graph)
            # Has no pending prereqs
            if not graph[step]
            # Not currently being worked on
            and step not in working_on
        ]
        # Assign work
        for step in available_steps:
            # busy lah
            if len(working_on) == WORKERS:
                break
            working_on[step] = seconds_required[step]

        if not working_on:
            break

        # Tick down seconds left (Very wasteful, should just jump till next task done.)
        for step in working_on.copy():
            working_on[step] -= 1
            if working_on[step] == 0:
                del working_on[step]
                del graph[step]
                graph = remove_prereq(graph, step)
        seconds += 1
    return seconds


if __name__ == '__main__':
    with open('day07-input.txt') as input_file:
        instructions = [instruction.strip() for instruction in input_file]
    # pt 1
    print(pt1(instructions))
    # pt 2
    print(pt2(instructions))
