import re
import math
from copy import deepcopy

def find_int(line, multiple=False):
    if multiple:
        return list(map(int, re.findall(r'\d+', line)))
    return int(re.search(r'\d+', line).group())

def monkey(lines):
    return {
        "id": find_int(lines[0]),
        "items": find_int(lines[1], True),
        "op": re.search(r'(old|\d+) (\+|\*) (old|\d+)', lines[2]).group(),
        "test": find_int(lines[3]),
        "pass": find_int(lines[4]),
        "fail": find_int(lines[5])
    }

def prepare(input):
    return [monkey(input[7*i:7*i+7]) for i in range(len(input) // 7 + 1)]
    
def inspect(input, rounds=20, should_worry=True):
    input = deepcopy(input)
    inspections = [0 for _ in range(len(input))]
    mod = math.prod([monkey["test"] for monkey in input])
    for _ in range(rounds):
        for i in range(len(input)):
            while input[i]["items"]:
                inspections[i] += 1
                item = input[i]["items"].pop(0)
                item = eval(input[i]["op"].replace('old', str(item)))
                if should_worry:
                    item = item // 3
                item = item % mod
                if item % input[i]["test"] == 0:
                    input[input[i]["pass"]]["items"].append(item)
                else:
                    input[input[i]["fail"]]["items"].append(item)
    return math.prod(sorted(inspections)[-2:])

def test(input):
    input = prepare(input)
    assert inspect(input) == 10605
    assert inspect(input, 10000, False) == 2713310158

def answer(input):
    input = prepare(input)
    print(inspect(input))
    print(inspect(input, 10000, False))
