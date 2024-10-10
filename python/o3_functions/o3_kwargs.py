""" kwargs """


def get_product(**data):
    """Prints the product details."""
    print(data["id"], data["name"])


get_product(id=1, name="Chanchirata", description="Python Developer")
get_product(id=2, name="Elliot", description="Python Developer")
