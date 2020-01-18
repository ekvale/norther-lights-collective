import itertools

text = "Password"

def encrypt(text, n):
    evens = []
    odds = []
    for _ in itertools.repeat(None, n):
        for char in range(len(text)):
            if char % 2 == 0:
                evens.append(text[char])
            else:
                odds.append(text[char])


encrypt(text, 3)