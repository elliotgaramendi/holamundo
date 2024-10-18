""" Management """

pets = [["Chocolate", 5], ["Chispa", 3], ["Rocky", 2], ["NN", 4], ["Doky", 1]]

names = [pet[0] for pet in pets]
print(names)
names = list(map(lambda pet: pet[0], pets))
print(names)

names = [pet[0] for pet in pets if pet[1] > 3]
print(names)
names = list(filter(lambda pet: pet[1] > 3, pets))
print(names)
