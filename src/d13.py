import json
import math

def prepare(input):
    return [
        (json.loads(input[3*i]), json.loads(input[3*i+1]))
        for i in range(len(input) // 3 + 1)
    ]

def get(arr, index):
    if index > len(arr) - 1:
        return False;
    return arr[index]

def compare(left, right):
    if isinstance(left, bool):
        return True

    if isinstance(right, bool):
        return False

    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right

    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    if isinstance(right, list) and isinstance(left, int):
        return compare([left], right)

    for i in range(max(len(left), len(right))):
        comparison = compare(get(left, i), get(right, i))
        if comparison is not None:
            return comparison

    return None

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if not compare(arr[j], arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
def part_one(input):
    return sum([
        i + 1
        for i, (left, right) in enumerate(input)
        if compare(left, right)
    ])

def part_two(input):
    packets = sum([[a, b] for (a, b) in input], []) + [[[2]]] + [[[6]]]
    packets = sort(packets)
    return math.prod([packets.index([[2]]) + 1, packets.index([[6]]) + 1])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 13
    assert part_two(input) == 140

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
