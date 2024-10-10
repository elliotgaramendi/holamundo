""" x-arguments """


def addition(*args):
    """Return the sum of all arguments."""
    result = 0
    for arg in args:
        result += arg
    print(result)


addition(1)
addition(5, 8)
addition(5, 8, 15)
addition(5, 8, 15, 31)
