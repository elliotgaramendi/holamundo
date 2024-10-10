""" Debugging """

def string_length(text):
    """Return the length of a string."""
    length = 0
    for _ in text:
        length += 1
    return length


RESULT = string_length("Happy Chanchito")
print(RESULT)
