from copy import deepcopy

shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)], # -
    [(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)], # +
    [(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)], # J
    [(0, 3), (0, 2), (0, 1), (0, 0)], # |
    [(0, 1), (1, 1), (0, 0), (1, 0)], # []
]

def prepare(input):
    return list(input)

def move(shape, direction):
    if direction == '<':
        return [(x - 1, y) for (x, y) in shape]
    elif direction == '>':
        return [(x + 1, y) for (x, y) in shape]
    elif direction == 'V':
        return [(x, y - 1) for (x, y) in shape]

def printb(board):
    for y in range(max([0] + list(board.values())) + 5, -1, -1):
        line = []
        for x in range(0, 7):
            line.append('#' if board.get((x, y), None) is not None else '.')
        print(str.join('', line))
    print('----')


def play(input, rocks=5):
    input, i = deepcopy(input), 1
    board = dict([((x, -1), -1) for x in range(0, 7)])

    for rock in range(rocks):
        current = shapes[rock % 5]
        dx, dy = 2, max(board.values()) + 3
        current = [(x + dx, y + dy) for (x, y) in current]

        while current is not None:        
            direction = input[i % len(input)]
            next_position = move(current, direction)
            i += 1
            print(direction)
            
            in_bounds = all([ x >= 0 and x <= 6 for (x, _) in next_position ])
            if not in_bounds:
                next_position = current

            next_down_position = move(next_position, 'V')
            can_move_down = all([ (x, y) not in board for (x, y) in next_down_position ])
            if can_move_down:
                current = next_down_position
            else:
                for (x, y) in next_position:
                    board[(x, y)] = y
                print(current)
                print(next_position)
                print('direction', direction)
                printb(board)
                current = None

    print(max(board.values()))
    return max(board.values())
    
def test(input):
    input = prepare(input)
    assert play(input) == 3068

def answer(input):
    input = prepare(input)
    print(part_one(input))
