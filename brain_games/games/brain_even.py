from brain_games.games import games_functions
import random


GAME_RANDOM_RANGE = (1, 99)
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_expression():
    number = random.randint(*GAME_RANDOM_RANGE)
    result = games_functions.is_even(number)
    result = 'yes' if result else 'no'
    return result, number
