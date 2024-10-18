""" List CRUD """

pets = ["Doky", "Rocky", "Chispa", "NN", "Chocolate"]
print(pets)

pets.append("Chanchito")
print(pets)

pets.insert(1, "Doky 2.0")
print(pets)

pets[4] = "NN 2.0"
print(pets)

pets.pop()
print(pets)

pets.pop(0)
print(pets)

pets.remove("NN 2.0")
print(pets)

pets.clear()
print(pets)
