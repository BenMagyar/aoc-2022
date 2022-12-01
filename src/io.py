import os

def clean(lines):
    return [line.rstrip() for line in lines]

def read_example(day):
    with open(os.path.join(os.getcwd(), "examples", day + ".txt")) as file:
        return clean(file.readlines())

def read_input(day):
    with open(os.path.join(os.getcwd(), "inputs", day + ".txt")) as file:
        return clean(file.readlines())