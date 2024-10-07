""" While """

NUMBER = 1

while NUMBER <= 10:
    print(NUMBER)
    NUMBER += 1

while True:
    command = input("$ ")
    print(command)
    if command.lower() == "exit":
        break
