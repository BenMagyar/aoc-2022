def prepare(input):
    return [
        (set(line[:len(line)//2]), set(line[len(line)//2:]))
        for line in input
    ]

def priority(item):
    return ord(item) - (96 if item.islower() else 38)
    
def part_one(input):
    return sum([
        priority(item)
        for a, b in input
        for item in a.intersection(b)
    ])

def part_two(input):
    groups, sum = [input[i:i+3] for i in range(0, len(input), 3)], 0
    for group in groups:
        overlap = None    
        for a, b in group:
            if not overlap:
                overlap = a.union(b)
            overlap = overlap.intersection(a.union(b))
        sum += priority(list(overlap)[0])
    return sum
    
def test(input):
    input = prepare(input)
    print(part_one(input))
    assert part_one(input) == 157
    assert part_two(input) == 70

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
