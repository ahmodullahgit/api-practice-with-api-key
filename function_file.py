def add(*args):
    total = 0
    for number in args:
        total += number
    return total

def sub(first, second):
    result = first - second
    return result

def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result

def devide(first, second):
    result = first / second
    return result
