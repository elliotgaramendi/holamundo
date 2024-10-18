""" List Iteration """

pets = ["Doky", "Rocky", "Chispa", "NN", "Chocolate"]
for pet in pets:
    print(pet)

for index, pet in enumerate(pets):
    print(index, pet)

for index, pet in enumerate(pets, start=1):
    print(index, pet)
