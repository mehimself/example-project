import sys

def subtract(x, y):
    """
    subtracts y from x
    """
    return x - y

def add(x, y):
    """
    Returns the sum of the two arguments.
    """
    return x + y


def square(x):
    """
    Returns square of the argument.
    """
    return x * x


def test_square():
    assert square(3.0) == 9.0


if __name__ == '__main__':

    # there are better ways to pass command line arguments
    # to a python code but this is not the point here
    x = float(sys.argv[-2])
    y = float(sys.argv[-1])

    result = add(x, y)
    print(result)
