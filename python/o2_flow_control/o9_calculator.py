# pylint: disable=invalid-name

""" Calculator """

print("Calculator")
print("To finish write exit")

result = None
baseNumber = input("Enter number 1: ")

while True:
    if result is None and baseNumber.lower() == "exit":
        break
    baseNumber = float(baseNumber)
    operator = input("Enter operator (+, -, *, /): ")
    if operator.lower() == "exit":
        break
    number2 = input("Enter number 2: ")
    if number2.lower() == "exit":
        break
    number2 = float(number2)
    if operator == "+":
        result = baseNumber + number2
    elif operator == "-":
        result = baseNumber - number2
    elif operator == "*":
        result = baseNumber * number2
    elif operator == "/":
        result = baseNumber / number2
    else:
        print("Invalid operator")
    print(f"{baseNumber} {operator} {number2} = {result}")
    baseNumber = result
