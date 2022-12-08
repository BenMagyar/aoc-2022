import math

def prepare(input):
    values = [list(map(int, list(line))) for line in input]
    return (values, len(values[0]), len(values))

def pair_range(xrange, yrange):
    for y in range(*yrange):
        for x in range(*xrange):
            yield (x, y)
    
def scan(input, ranges, initial=-1, is_inward=True):
    visible = {}
    for xrange, yrange in ranges:
        compare = initial
        for x, y in pair_range(xrange, yrange):
            if is_inward and input[y][x] > compare:
                visible[(x,y)], compare = 1, input[y][x]
            elif not is_inward and input[y][x] < compare:
                visible[(x,y)] = 1
            elif not is_inward and input[y][x] >= compare:
                visible[(x,y)] = 1
                break
                
    return visible

def part_one(input, width, height):
    xranges = [(0, width, 1), (width - 1, -1, -1)]
    yranges = [(0, height, 1), (height - 1, -1, -1)]
    ranges = [(x, y) for x in xranges for y in yranges]
    return sum([
        sum(scan(input, [pair]).values())
        for pair in ranges
    ])

def part_two(input, width, height):
    score = {}
    for x, y in pair_range((width,), (height,)):
        ranges = [
            ((x-1, -1, -1), (y, y+1)),
            ((x+1, width, 1), (y, y+1)),
            ((x, x+1), (y-1, -1, -1)),
            ((x, x+1), (y+1, height, 1)),
        ]
        score[(x, y)] = math.prod([
            sum(scan(input, [pair], input[y][x], False).values())
            for pair in ranges
        ])
    return max(score.values())

def test(input):
    input = prepare(input)
    assert part_one(*input) == 21
    assert part_two(*input) == 8

def answer(input):
    input = prepare(input)
    print(part_one(*input))
    print(part_two(*input))
