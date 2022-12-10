def convert(line):
    op, value, *_ = line.split(' ') + [None]
    return (op, int(value), 2) if op == 'addx' else (op, 0, 1)

def prepare(input):
    return [convert(line) for line in input]

def draw(x, cycle, image):
    position = cycle % 40
    if position == 0:
        image.append([])
    is_captured = x - 1 <= position <= x + 1
    image[-1].append('#' if is_captured else ' ')
    return image
    
def program(input, capture=[20, 60, 100, 140, 180, 220]):
    x, cycle, strengths, image = 1, 0, 0, []
    for _, inc, cycles in input:        
        for i in range(cycles):
            image = draw(x, cycle, image)
            cycle += 1
            if cycle in capture:
                strengths += (cycle * x)
        x += inc
    for line in image:
        print(str.join('', line))
    return strengths
    
def test(input):
    input = prepare(input)
    assert program(input) == 13140

def answer(input):
    input = prepare(input)
    print(program(input))
