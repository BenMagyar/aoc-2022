SHAPES = {'X': 1, 'Y': 2, 'Z': 3}
POINTS = {'lost': 0, 'draw': 3, 'won': 6}
PLAYER_MAP = {'X': 'A', 'Y': 'B', 'Z': 'C'}
WIN_OUTCOMES = { 'X': 'C', 'Y': 'A', 'Z': 'B' }
LOSS_MOVES = {'A': 'Z', 'B': 'X', 'C': 'Y'}
OUTCOMES = { 'X': 'loss', 'Y': 'draw', 'Z': 'win'}

win_moves = {opp: move for move, opp in WIN_OUTCOMES.items()}
inverse_player_map = {opp: move for move, opp in PLAYER_MAP.items()}

def prepare(input):
    return [str.split(game) for game in input]

def play(opponent, move):
    if WIN_OUTCOMES[move] == opponent:
        return POINTS['won'] + SHAPES[move]
    elif PLAYER_MAP[move] == opponent:        
        return POINTS['draw'] + SHAPES[move]
    else:
        return POINTS['lost'] + SHAPES[move]

def play_for_outcome(opponent, outcome):
    if OUTCOMES[outcome] == 'win':
        return play(opponent, win_moves[opponent])
    elif OUTCOMES[outcome] == 'draw':
        return play(opponent, inverse_player_map[opponent])
    else:
        return play(opponent, LOSS_MOVES[opponent])
    
def part_one(input):
    return sum([play(*game) for game in input])

def part_two(input):
    return sum([play_for_outcome(*game) for game in input])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 15
    assert part_two(input) == 12

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
