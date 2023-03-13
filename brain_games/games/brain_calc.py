from random import choice
from brain_games.games import games_functions


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'What is the result of the expression?'


def make_expression():
    number1 = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    number2 = games_functions.get_random_value_by_range(GAME_RANDOM_RANGE)
    operator, operator_symbol = choice([
        (lambda x, y: x + y, '+'),
        (lambda x, y: x - y, '-'),
        (lambda x, y: x * y, '*'),
    ])
    result = operator(number1, number2)
    return result, f'{number1} {operator_symbol} {number2}'
