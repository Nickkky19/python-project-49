from math import gcd
import random


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_expression():
    number1 = random.randint(*GAME_RANDOM_RANGE)
    number2 = random.randint(*GAME_RANDOM_RANGE)
    result = gcd(number1, number2)
    return result, f'{number1} {number2}'
