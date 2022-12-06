def find_distinct(input, count):
    for i in range(len(input)):
        if len(set(list(input[max(i-count,0):i]))) == count:
            return i
    
def test(input):
    assert find_distinct(input, 4) == 7
    assert find_distinct(input, 14) == 19

def answer(input):
    print(find_distinct(input, 4))
    print(find_distinct(input, 14))
