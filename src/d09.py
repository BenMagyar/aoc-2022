import math

def prepare(input):
    directions = []
    for line in input:
        direction, amt = line.split(' ')
        directions.append((direction, int(amt)))
    return directions

def move_step(direction, coordinate):
    x, y = coordinate
    if direction == 'R':
        return (x + 1, y)
    elif direction == 'L':
        return (x - 1, y)
    elif direction == 'U':
        return (x, y + 1)
    elif direction == 'D':
        return (x, y - 1)

def sign(num):
    return int(math.copysign(1, num)) if num != 0 else 0

def move_tail(head, tail):
    (xh, yh), (xt, yt) = head, tail
    xd, yd = xh - xt, yh - yt
    if abs(xd) > 1 or abs(yd) > 1:
        return (xt + sign(xd), yt + sign(yd))
    return (xt, yt)
    
def snake(input, knots=2):
    knots, touched = [(0, 0) for _ in range(knots)], {}
    for direction, amt in input:
        for _ in range(amt):
            knots[0] = move_step(direction, knots[0])
            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i-1], knots[i])
                if i == len(knots) - 1:
                    touched[knots[i]] = 1
    return sum(touched.values())

def test(input):
    input = prepare(input)
    # assert snake(input) == 13
    assert snake(input, 10) == 36

def answer(input):
    input = prepare(input)
    print(snake(input))
    print(snake(input, 10))