import random


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(temp_number):
    return temp_number % 2 == 0


def make_expression():
    number = random.randint(*GAME_RANDOM_RANGE)
    result = is_even(number)
    result = 'yes' if result else 'no'
    return result, number
