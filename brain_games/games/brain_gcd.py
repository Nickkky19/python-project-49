from math import gcd
from brain_games.games import games_functions


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_expression():
    number1 = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    number2 = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    result = gcd(number1, number2)
    return result, f'{number1} {number2}'
