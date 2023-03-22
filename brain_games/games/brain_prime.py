from brain_games.games import games_functions
import random


GAME_RANDOM_RANGE = (2, 99)
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_expression():
    number = random.randint(*GAME_RANDOM_RANGE)
    result = games_functions.is_prime(number)
    result = 'yes' if result else 'no'
    return result, number
