def prepare(input):
    inv = [[]]
    [inv.append([]) if not cal else inv[-1].append(int(cal)) for cal in input]
    return inv
    
def part_one(input):
    return max([sum(elf) for elf in input])

def part_two(input):
    return sum(sorted([sum(elf) for elf in input])[-3:])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 24000
    assert part_two(input) == 45000

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
