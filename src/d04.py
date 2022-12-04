def prepare(input):
    split = lambda p: list(map(int, p.split('-')))
    pairs = [line.split(',') for line in input]
    return [(split(a), split(b)) for (a, b) in pairs]
    
def part_one(input):
    overlaps = lambda a, b: a[0] >= b[0] and a[1] <= b[1]
    return sum([
        1 if overlaps(a, b) or overlaps(b, a) else 0
        for a, b in input
    ])

def part_two(input):
    overlaps = lambda a, b: a[0] <= b[0] and a[1] >= b[0]
    return sum([
        1 if overlaps(a, b) or overlaps(b, a) else 0
        for a, b in input
    ])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 2
    assert part_two(input) == 4

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
