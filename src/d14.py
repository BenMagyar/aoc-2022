from copy import deepcopy

def coord(line):
    return (int(line.split(',')[0]), int(line.split(',')[1]))

def prepare(input):
    graph = {}
    for line in input:
        coords = line.split(' -> ')
        (px, py) = coord(coords[0])
        while len(coords) > 0:
            (cx, cy) = coord(coords.pop(0))
            for x in range(min(cx, px), max(cx, px) + 1):
                for y in range(min(cy, py), max(cy, py) + 1):
                    graph[(x, y)] = '#'
            (px, py) = (cx, cy)
    return graph
    
def simulate(input, has_floor = False):
    input = deepcopy(input)
    (sx, sy) = sand = initial_sand = (500, 0)
    max_y = max([y for (_, y) in input.keys()])
    if has_floor:
        max_y = max_y + 2

    while sy < max_y:
        (sx, sy) = sand
        next_position = next((
            (sx + dx, sy + dy)
            for (dx, dy) in [(0, 1), (-1, 1), (1, 1)]
            if input.get((sx + dx, sy + dy), None) is None 
                and (not has_floor or sy + dy < max_y)
        ), None)
  
        if next_position is None:
            input[(sand)] = 'o'
            if sand == initial_sand:
                break;
            sand = initial_sand
        else:
            sand = next_position
    
    return len([
        value for value in input.values()
        if value == 'o'
    ])
    
def test(input):
    input = prepare(input)
    assert simulate(input) == 24
    assert simulate(input, True) == 93

def answer(input):
    input = prepare(input)
    print(simulate(input))
    print(simulate(input, True))
