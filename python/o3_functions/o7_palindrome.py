""" Palindrome """


def reverse(text):
    """Return the reverse of a string."""
    inverted_text = ""
    for char in text:
        inverted_text = char + inverted_text
    return inverted_text


def is_palindrome(text):
    """Return True if the text is a palindrome."""
    text = text.lower()
    return text == reverse(text)


print("oxo", is_palindrome("oxo"))
print("abba", is_palindrome("abba"))
print("Reconocer", is_palindrome("Reconocer"))
print("Amo la paloma", is_palindrome("Amo la paloma"))
