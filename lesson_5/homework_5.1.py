import string
import keyword

text = input("Введи назву змінної: \n ")

if (text.islower() and
    not text[0].isdigit() and
    not text in keyword.kwlist and
    text.count('_') != len(text) and
    not ' ' in text and
    not any((char in string.punctuation and char != '_') for char in text)):
    print("все ок")
else:
    print("не можна")

