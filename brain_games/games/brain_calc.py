import random


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'What is the result of the expression?'


def make_expression():
    number1 = random.randint(*GAME_RANDOM_RANGE)
    number2 = random.randint(*GAME_RANDOM_RANGE)
    operator, operator_symbol = random.choice([
        (lambda x, y: x + y, '+'),
        (lambda x, y: x - y, '-'),
        (lambda x, y: x * y, '*'),
    ])
    result = operator(number1, number2)
    return result, f'{number1} {operator_symbol} {number2}'
