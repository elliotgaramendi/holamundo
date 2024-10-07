""" Comparisons """

age = int(input("Enter your age: "))
money = bool(int(input("¿Do you have money? Yes(1) or No(0): ")))

MESSAGE = "You can enter" if age >= 18 and money else "You can't enter"
print(MESSAGE)
