# pylint: disable=invalid-name

""" String methods """

animal = "haPPy chanChito"
print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())

animal = " haPPy chanChito "
print(animal)
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.strip().title())

animal = "haPPy ChanChito"
print(animal.find("Ch"))
print(animal.find("cH"))
print(animal.replace("nCh", "nj"))
print("Ch" in animal)
print("ch" in animal)
print("Ch" not in animal)
