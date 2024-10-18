""" Lambda """

pets = [["Chocolate", 5], ["Chispa", 3], ["Rocky", 2], ["NN", 4], ["Doky", 1]]

sortedPets = sorted(pets, key=lambda pet: pet[1])
print(sortedPets)
