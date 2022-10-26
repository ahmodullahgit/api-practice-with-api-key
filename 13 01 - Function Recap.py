# find maximum number from three number
def maximum_value(a, b, c):
    """
    this will find out the maximum value from 3 numbers.
    :param a: first number
    :param b: second number
    :param c: third number
    :return: this will return the maximum number.
    """
    if b < a > c:
        print(a)
    elif a < b > c:
        print(b)
    else:
        print(c)
maximum_value(45, 32, 13)

# Calculate the area of circle from the following radius

def circle_area(radius):
    """
    this function will calculate the area of circle from given radius.
    :param radius: it takes a number which can be float or integer.
    :return: it will return the area of circle.
    """
    area = 3.14 * radius * radius
    return area
print(circle_area(4))

# args related function
def sum(*args):
    """
    this function will calculate the sum of unlimited numbers using args formula.
    :param args: it can be multiple number of integer or float
    :return: this will return the total sum of numbers which are provided.
    """
    total = 0
    for num in args:
        total += num
    return total
print(sum(4,6,7,8,4,4))