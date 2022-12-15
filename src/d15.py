import re

def prepare(input):
    return [
        list(map(int, re.findall(r'\d+', line)))
        for line in input
    ]

def distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

def union(ranges):
    ranges = sorted(ranges)
    union = [ranges.pop(0)]
    for start, end in sorted(ranges):
        if start <= union[-1][1]:
            union[-1] = (union[-1][0], max(union[-1][1], end))
        else:
            union.append([start, end])
    return union

def negate(ranges):
    ranges, last, union = sorted(ranges), 0, []
    for start, end in ranges:
        union.append((last, start))
        last = end
    return union

def scan_y(input, target=10):
    ranges = []
    for cx, cy, sx, sy in input:
        dist = distance(cx, cy, sx, sy)
        ys = [cy - dist, cy + dist]
        min_y, max_y = min(ys), max(ys)
        
        target_dist = None
        if target >= cy and target < max_y:
            target_dist = target - cy
        elif target < cy and target > min_y:
            target_dist = cy - target
        
        if target_dist is not None:
            width = dist - target_dist
            ranges.append((cx - width, cx + width))

    return union(ranges)

def part_one(input, target=10):
    return sum([
        end - start for (start, end) in scan_y(input, target)
    ])

def part_two(input, max_y):
    possible = {}
    for y in range(0, max_y):
        scan = scan_y(input, y)
        open = negate(scan)
        exists = {}
        
        for xrange in open:
            for x in range(*xrange):
                dist_left, dist_right = x - min(xrange), max(xrange) - x
                if dist_left == dist_right:
                    width, exists[x] = len(xrange), True
                    if x in possible:
                        start_y, height, widths = possible[x]
                        possible[x] = (start_y, height + 1, widths + [width])
                    else:
                        possible[x] = (y, 1, [width])
        
        for x in list(possible.keys()):
            if x not in exists:
                start_y, height, widths = possible.pop(x)
                middle = len(widths) // 2
                if (widths[-1:middle]) == widths[:middle]:
                    return (x * 4000000) + (start_y + middle)
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 26
    assert part_two(input, 20) == 56000011

def answer(input):
    input = prepare(input)
    print(part_one(input, 2000000))
    print(part_two(input, 4000000))
