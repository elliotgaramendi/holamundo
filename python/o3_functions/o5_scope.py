""" Scope """


def greet():
    """Return a greeting."""
    greeting = "Hello"
    return greeting


def to_greet(name):
    """Return a greeting with a name."""
    greeting = f"Hello {name}"
    return greeting


print(greet())
print(to_greet("Chanchirata"))
