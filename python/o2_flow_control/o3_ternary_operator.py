""" Ternary operator """

AGE = 28
MESSAGE = "You are " + ("an older adult" if AGE >= 60 else "an adult" if AGE >= 18 else "a child")
print(MESSAGE)
