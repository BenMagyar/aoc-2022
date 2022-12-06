import os

def clean(lines):
    lines = [line.rstrip() for line in lines]
    return lines[0] if len(lines) == 1 else lines

def read_example(day):
    with open(os.path.join(os.getcwd(), "examples", day + ".txt")) as file:
        return clean(file.readlines())

def read_input(day):
    with open(os.path.join(os.getcwd(), "inputs", day + ".txt")) as file:
        return clean(file.readlines())