import random, string
import pandas as pd

# choosing variables for program

Letter1 = input('Enter a vowel "v" or a consonant "c" or any letter "l": ')
Letter2 = input('Enter a vowel "v" or a consonant "c" or any letter "l": ')
Letter3 = input('Enter a vowel "v" or a consonant "c" or any letter "l": ')
Letter4 = input('Enter a vowel "v" or a consonant "c" or any letter "l": ')
Letter5 = input('Enter a vowel "v" or a consonant "c" or any letter "l": ')

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

# check for baby names
baby = pd.read_csv('baby.txt')

# working with the entries to generate names


def generator():
    if Letter1 == "v":
        first = random.choice(vowels)
    elif Letter1 == "c":
        first = random.choice(consonants)
    elif Letter1 == "l":
        first = random.choice(letter)
    else:
        first = Letter1

    if Letter2 == "v":
        second = random.choice(vowels)
    elif Letter2 == "c":
        second = random.choice(consonants)
    elif Letter2 == "l":
        second = random.choice(letter)
    else:
        second = Letter2

    if Letter3 == "v":
        third = random.choice(vowels)
    elif Letter3 == "c":
        third = random.choice(consonants)
    elif Letter3 == "l":
        third = random.choice(letter)
    else:
        third = Letter3

    if Letter4 == "v":
        fourth = random.choice(vowels)
    elif Letter4 == "c":
        fourth = random.choice(consonants)
    elif Letter4 == "l":
        fourth = random.choice(letter)
    else:
        fourth = Letter4

    if Letter5 == "v":
        fifth = random.choice(vowels)
    elif Letter5 == "c":
        fifth = random.choice(consonants)
    elif Letter5 == "l":
        fifth = random.choice(letter)
    else:
        fifth = Letter5

    name = first + second + third + fourth + fifth

    return name


# fullname = generator()

name2 = zip(baby['NAME'])

for i in range(50):
    # if generator() == name2:

    print(generator())
