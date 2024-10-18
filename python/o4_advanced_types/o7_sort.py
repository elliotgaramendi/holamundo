""" Sort """

numbers = [5, 3, 1, 4, 2, 6, 7, 8]
print(numbers)

sortedNumbers = sorted(numbers)
print(sortedNumbers)
print(numbers)

numbers.sort()
print(numbers)

pets = [["Chocolate", 5], ["Chispa", 3], ["Rocky", 2], ["NN", 4], ["Doky", 1]]
print(pets)


def order(pet):
    """Return the second element of the pet list, which is the order key."""
    return pet[1]


sortedPets = sorted(pets, key=order)
print(sortedPets)

print(pets)
pets.sort(key=order, reverse=True)
print(pets)
