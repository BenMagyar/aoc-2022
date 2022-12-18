def prepare(input):
    return [
        tuple(map(int, (x, y, z)))
        for (x, y, z) in [
            line.split(',')
            for line in input
        ]
    ]

def neighbors(cube):
    (x, y, z) = cube
    return [
        (x + dx, y + dy, z + dz) 
        for (dx, dy, dz) in [
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1),
        ]
    ]

def vrange(cubes, axis):
    values = [cube[axis] for cube in cubes]
    return (min(values) - 1, max(values) + 1)

def in_range(value, range):
    return value >= range[0] and value <= range[1]

def surface_expand(cubes):
    xr, yr, zr = vrange(cubes, 0), vrange(cubes, 1), vrange(cubes, 2)
    
    active, searched, surfaces = [(xr[0], yr[0], zr[0])], set(), set()
    while len(active) > 0:
        current = active.pop(0)
        cx, cy, cz = current
        
        if current in searched:
            continue
        else:
            searched.add(current)

        if not (in_range(cx, xr) and in_range(cy, yr) and in_range(cz, zr)):
            continue

        for neighbor in neighbors(current):
            if neighbor in cubes:
                if ((current, neighbor) not in surfaces):
                    surfaces.add((current, neighbor))
            elif neighbor not in searched:  
                active.append(neighbor)

    return len(surfaces)
    
def surface(cubes):
    area = sum([
        len([
            neighbor
            for neighbor in neighbors(cube)
            if neighbor not in cubes
        ])
        for cube in cubes
    ])
    return area
    
def test(input):
    input = prepare(input)
    assert surface(input) == 64
    assert surface_expand(input) == 58

def answer(input):
    input = prepare(input)
    print(surface(input))
    print(surface_expand(input))
