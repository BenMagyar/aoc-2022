import math
import re
from copy import deepcopy

def prepare(input):
    return [line.split(' ') for line in input]

class Dir:
    def __init__(self, parent):
        self.files = {}
        self.subdirs = {}
        self.parent = parent

    def dir(self, name):
        if name not in self.subdirs:
            self.subdirs[name] = Dir(self)
        return self.subdirs[name]

    def file(self, name, size):
        self.files[name] = int(size)

    def size(self):
        return sum(self.files.values()) + sum([subdir.size() for subdir in self.subdirs.values()])

    def traverse(self):
        yield self
        for subdir in self.subdirs.values():
            yield from subdir.traverse()

class Term:
    def __init__(self, lines):
        self.root = Dir(None)
        self.pwd = self.root
        self.lines = deepcopy(lines)

    def is_cmd(self, line):
        return line is not None and line[0] == '$'

    def next(self):
        return self.lines.pop(0) if len(self.lines) > 0 else None

    def cd(self, arg0):
        if arg0 == "/":
            self.pwd = self.root
        elif arg0 == "..":
            self.pwd = self.pwd.parent
        else:
            self.pwd = self.pwd.dir(arg0)

    def ls(self):
        while (line := self.next()) is not None and not self.is_cmd(line):
            dir_or_size, name = line
            if re.match(r'\d+', dir_or_size):
                self.pwd.file(name, dir_or_size)
        if line is not None:
            self.lines.insert(0, line)

    def process(self):
        while (line := self.next()) is not None:
            if self.is_cmd(line):
                getattr(self, line[1])(*line[2:])
    
def part_one(input):
    term = Term(input)
    term.process()

    return sum([
        size if (size := dir.size()) < 100000 else 0
        for dir in term.root.traverse()
    ])

def part_two(input):
    term = Term(input)
    term.process()

    required = 30000000 - (70000000 - term.root.size())

    return min([
        size if (size := dir.size()) > required else math.inf
        for dir in term.root.traverse()
    ])
    
def test(input):
    input = prepare(input)
    assert part_one(input) == 95437
    assert part_two(input) == 24933642

def answer(input):
    input = prepare(input)
    print(part_one(input))
    print(part_two(input))
