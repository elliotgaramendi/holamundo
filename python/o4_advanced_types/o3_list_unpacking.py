""" Unpacking Lists """

pets = ["Doky", "Rocky", "Chispa"]
first, second, third = pets
print(first, second, third)

pets = ["Doky", "Rocky", "Chispa", "NN", "Chocolate"]
first, *rest = pets
print(first, rest)

numbers = list(range(16))
first, second, *rest = numbers
print(first, second, rest)

first, *rest, last = numbers
print(first, rest, last)

first, second, *rest, penultimate, last = numbers
print(first, second, rest, penultimate, last)
