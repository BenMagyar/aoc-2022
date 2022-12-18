import re

pattern = r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (([A-Z\,?\s?]{2})+)"

def prepare(input):
    graph, rates = {}, {}
    for line in input:
        source, rate, *dests = re.search(pattern, line).groups()
        graph[source] = list(map(lambda d: d.strip(), dests[0].split(',')))
        rates[source] = int(rate)
    return graph, rates

def search(graph, rates, mins):
    searched = {}


    def search_remaining(current, remaining, open, flow):  
        if remaining <= 0:
            return (flow, open)

        key = (current, remaining, tuple(sorted(open)))
        if key in searched:
            value, used = searched[key]
            return (value, tuple(sorted(set(open + used))))

        current_rate = (remaining - 1) * rates[current]

        optimal = (0, None)
        for neighbor in graph[current]:
            if current not in open and rates[current] > 0:
                value, used = search_remaining(neighbor, remaining - 2, open + (current,), flow)
                value += current_rate
                if max(optimal[0], value) == value:
                    optimal = (value, used)
            value, used = search_remaining(neighbor, remaining - 1, open, flow)
            if max(optimal[0], value) == value:
                optimal = (value, used)

        searched[key] = optimal
        return searched[key]

    value, _ = search_remaining('AA', mins, (),  0)
    return value, searched

def is_empty_intersection(t1, t2):
    return (not any([element in t1 for element in t2]) and 
        not any([element in t2 for element in t1]))

def part_one(input):
    return search(*input, 30)[0]

def part_two(input):
    (_, searched), optimal = search(*input, 26), 0
    b = None
    for (c1, r1, o1) in searched:
        for (c2, r2, o2) in searched:
            (f1, u1), (f2, u2) = searched[(c1, r1, o1)], searched[(c2, r2, o2)]
            if is_empty_intersection(u1, u2):
                optimal = max(optimal, f1 + f2)
                if optimal == f1 + f2:
                    b = (u1, u2)
    print(b)
    return optimal
    
def test(input):
    input = prepare(input)
    # assert part_one(input) == 1651
    print(part_two(input))
    assert part_two(input) == 1707

def answer(input):
    input = prepare(input)
    print(search(*input))
