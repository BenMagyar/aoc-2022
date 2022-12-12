import math

def prepare(input):
    height = lambda c: ord(c) - 96
    graph, start, end = {}, None, None
    for y in range(len(input)):
        for x in range(len(input[y])):
            if (value := input[y][x]) == 'S':
                start, graph[(x, y)] = (x, y), height('a')
            elif value == 'E':
                end, graph[(x, y)] = (x, y), height('z')
            else:
                graph[(x, y)] = height(input[y][x])
    return (start, end, graph)

def neighbors(graph, x, y):
    for (xd, yd) in [(-1,0),(1,0),(0,-1),(0,1)]:
        if graph.get((x + xd, y + yd), math.inf) - graph[(x, y)] <= 1:
            yield (x + xd, y + yd)

def search(graph, starts, end):
    active, found, dist = [(s,) for s in starts], [], {}
    
    while len(active) > 0:
        current = active.pop()
        dist[current[-1]] = len(current)

        if current[-1] == end:
            found.append(current[:-1])
        
        for neighbor in neighbors(graph, *current[-1]):
            if len(current) + 1 < dist.get(neighbor, math.inf):
                active.append(current + (neighbor,))
            
    return found
    
def part_one(start, end, graph):
    return min([len(path) for path in search(graph, [start], end)])

def part_two(_, end, graph):
    starts = [
        coord
        for coord, value in graph.items()
        if value == 1
    ]

    return min([len(path) for path in search(graph, starts, end)])

def test(input):
    input = prepare(input)
    assert part_one(*input) == 31
    assert part_two(*input) == 29

def answer(input):
    input = prepare(input)
    print(part_one(*input))
    print(part_two(*input))
