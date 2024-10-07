""" For """

numberToSearch = int(input("Enter a number to search: "))

for number in range(10):
    print(number)
    if number == numberToSearch:
        print("Found")
        break
else:
    print("Not found")

for character in "Happy Chanchito":
    print(character)
