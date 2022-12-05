import re
from collections import defaultdict
from copy import deepcopy

def prepare(input):
    divider = input.index('')
    crate_lines, instruction_lines = input[:divider], input[divider+1:]
    count = max(map(int, re.findall(r'\d+', crate_lines.pop())))
    
    crates = defaultdict(list)
    for i in range(count):
        for line in crate_lines:
            if (value := (line + " " * 5 * count)[(4 * i) + 1]) != ' ':
                crates[i + 1].insert(0, value)

    instructions = [
        list(map(int, re.search(r'(\d+) from (\d+) to (\d+)', line).groups()))
        for line in instruction_lines
    ]

    return deepcopy((count, crates, instructions))
    
def crane(input, lift_all = False):
    count, crates, instructions = input
    for amt, source, target in instructions:
        stack = [crates[source].pop() for _ in range(amt)]
        if lift_all:
            stack.reverse()
        for crate in stack:
            crates[target].append(crate)
    return str.join('', [crates[i + 1].pop() for i in range(count)])
    
def test(input):
    assert crane(prepare(input)) == "CMZ"
    assert crane(prepare(input), lift_all=True) == "MCD"

def answer(input):
    print(crane(prepare(input)))
    print(crane(prepare(input), lift_all=True))
